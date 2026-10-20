#!/usr/bin/env python3
"""Attention map of a screenshot (Pillow only).

Usage: python sightline.py <screenshot> [--out map.png] [--regions 3]

Blurs the screenshot (the squint test), measures local luminance contrast and saturation, and
reports the strongest attention regions top to bottom: where the eye lands first, second, third.
Writes a map image with the regions boxed when --out is given. The critic still looks at the
screenshot; this gives it numbers to point at.
"""
import argparse
import json
import sys

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps


def attention(img):
    w, h = img.size
    scale = 240 / w
    small = img.convert("RGB").resize((240, max(1, int(h * scale))))
    lum = ImageOps.autocontrast(small.convert("L"))
    blurred = lum.filter(ImageFilter.GaussianBlur(6))
    local = ImageChops.difference(lum, blurred)  # local contrast after a squint
    hsv = small.convert("HSV")
    sat = hsv.getchannel("S")
    sat_blur = sat.filter(ImageFilter.GaussianBlur(3))
    # weight: local contrast + 0.6 × saturation, then blur so regions form
    combined = ImageChops.add(local, ImageOps.autocontrast(sat_blur).point(lambda v: int(v * 0.6)))
    heat = combined.filter(ImageFilter.GaussianBlur(5))
    heat = ImageOps.autocontrast(heat)
    return heat, scale


def regions(heat, n, box=48, min_gap=36):
    w, h = heat.size
    px = heat.load()
    cells = []
    for y in range(0, h - box + 1, 8):
        for x in range(0, w - box + 1, 8):
            s = 0
            for yy in range(y, y + box, 4):
                for xx in range(x, x + box, 4):
                    s += px[xx, yy]
            cells.append((s, x, y))
    cells.sort(reverse=True)
    picked = []
    for s, x, y in cells:
        if all(abs(x - px_) >= min_gap or abs(y - py_) >= min_gap for _, px_, py_ in picked):
            picked.append((s, x, y))
        if len(picked) == n:
            break
    top = picked[0][0] if picked else 1
    return [{"x": x, "y": y, "w": box, "h": box, "weight": round(s / top, 3)} for s, x, y in picked]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("screenshot")
    ap.add_argument("--out")
    ap.add_argument("--regions", type=int, default=3)
    a = ap.parse_args()
    img = Image.open(a.screenshot)
    heat, scale = attention(img)
    regs = regions(heat, a.regions)
    inv = 1 / scale
    for i, r in enumerate(regs, 1):
        r.update({"rank": i, "x": int(r["x"] * inv), "y": int(r["y"] * inv), "w": int(r["w"] * inv), "h": int(r["h"] * inv)})
    order = sorted(regs, key=lambda r: r["rank"])
    out = {
        "source": a.screenshot,
        "size": [img.width, img.height],
        "regions": order,
        "reading": "rank 1 is where the eye lands first after a squint; compare with the brief's one job",
    }
    if a.out:
        canvas = img.convert("RGB")
        hm = heat.resize(canvas.size).convert("RGB")
        blend = Image.blend(canvas, hm, 0.55)
        d = ImageDraw.Draw(blend)
        for r in order:
            d.rectangle([r["x"], r["y"], r["x"] + r["w"], r["y"] + r["h"]], outline=(255, 64, 32), width=max(2, img.width // 300))
            d.text((r["x"] + 4, r["y"] + 4), str(r["rank"]), fill=(255, 64, 32))
        blend.save(a.out)
        out["map"] = a.out
    sys.stdout.write(json.dumps(out, indent=1) + "\n")


if __name__ == "__main__":
    main()
