#!/usr/bin/env python3
"""Extract visual tokens from a reference image into JSON (Pillow only).

Usage: python extract-tokens.py <image> [--out tokens.json] [--colors 8]

Output: dominant colours (hex, share, role guess), background and ink picks with their contrast
ratio, whitespace ratio, and an estimated base spacing unit from the run lengths of the
background colour. These are measurements for the interview's "visual world" question; they are
not a design. Mechanics and measurements transfer, looks do not.
"""
import argparse
import json
import sys
from collections import Counter

from PIL import Image, ImageFilter


def srgb_to_lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(rgb):
    r, g, b = (srgb_to_lin(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def hexs(rgb):
    return "#%02x%02x%02x" % rgb


def saturation(rgb):
    mx, mn = max(rgb), min(rgb)
    return 0 if mx == 0 else (mx - mn) / mx


def dominant_colors(img, n):
    small = img.convert("RGB").resize((200, int(200 * img.height / img.width) or 1))
    q = small.quantize(colors=n, method=Image.Quantize.MEDIANCUT)
    palette = q.getpalette()[: n * 3]
    counts = Counter(q.get_flattened_data() if hasattr(q, "get_flattened_data") else q.getdata())
    total = sum(counts.values())
    out = []
    for idx, cnt in counts.most_common():
        rgb = tuple(palette[idx * 3 : idx * 3 + 3])
        out.append({"hex": hexs(rgb), "rgb": rgb, "share": round(cnt / total, 4)})
    return out


def guess_roles(colors, min_share=0.004):
    """bg = the most common colour; ink = the darkest colour with a real share (text is thin, so it is
    never the most common); accent = the most saturated of the rest."""
    bg = colors[0]
    real = [c for c in colors if c is not bg and c["share"] >= min_share]
    ink = min(real, key=lambda c: luminance(c["rgb"])) if real else colors[-1]
    accents = [c for c in real if c is not ink and saturation(c["rgb"]) > 0.35]
    accent = max(accents, key=lambda c: saturation(c["rgb"]) * (0.3 + c["share"])) if accents else None
    for c in colors:
        c["role"] = "background" if c is bg else "ink" if c is ink else "accent" if c is accent else "secondary"
    return bg, ink, accent


def spacing_unit(img, bg_rgb, tol=18):
    """Estimate the base spacing unit from horizontal runs of background colour between other content."""
    g = img.convert("RGB")
    w, h = g.size
    px = g.load()
    runs = Counter()
    step = max(1, h // 200)
    for y in range(0, h, step):
        run = 0
        for x in range(w):
            r, gg, b = px[x, y]
            if abs(r - bg_rgb[0]) < tol and abs(gg - bg_rgb[1]) < tol and abs(b - bg_rgb[2]) < tol:
                run += 1
            else:
                if 4 <= run <= 200:
                    runs[run] += 1
                run = 0
    if not runs:
        return None, {}
    # the base unit is the smallest run length among the most common ones, rounded to 4
    common = [r for r, _ in runs.most_common(12)]
    base = min(common)
    base = max(4, int(round(base / 4.0) * 4))
    hist = {str(r): c for r, c in sorted(runs.most_common(8))}
    return base, hist


def whitespace_ratio(img, bg_rgb, tol=18):
    g = img.convert("RGB").resize((160, int(160 * img.height / img.width) or 1))
    px = list(g.get_flattened_data() if hasattr(g, "get_flattened_data") else g.getdata())
    bg = sum(1 for r, gg, b in px if abs(r - bg_rgb[0]) < tol and abs(gg - bg_rgb[1]) < tol and abs(b - bg_rgb[2]) < tol)
    return round(bg / len(px), 3)


def edge_density(img):
    e = img.convert("L").filter(ImageFilter.FIND_EDGES)
    hist = e.histogram()
    strong = sum(hist[48:])
    return round(strong / sum(hist), 4)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("image")
    ap.add_argument("--out")
    ap.add_argument("--colors", type=int, default=16)
    a = ap.parse_args()
    img = Image.open(a.image)
    colors = dominant_colors(img, a.colors)
    bg, ink, accent = guess_roles(colors)
    unit, hist = spacing_unit(img, bg["rgb"])
    out = {
        "source": a.image,
        "size": [img.width, img.height],
        "colors": colors,
        "background": bg["hex"],
        "ink": ink["hex"],
        "ink_contrast": round(contrast(ink["rgb"], bg["rgb"]), 2),
        "accent": accent["hex"] if accent else None,
        "accent_contrast_on_background": round(contrast(accent["rgb"], bg["rgb"]), 2) if accent else None,
        "whitespace_ratio": whitespace_ratio(img, bg["rgb"]),
        "edge_density": edge_density(img),
        "spacing_unit_estimate_px": unit,
        "background_run_lengths": hist,
        "note": "measurements of a reference; transfer the ratios and the contrast, not the colours themselves",
    }
    text = json.dumps(out, indent=1)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(text)
        print(a.out)
    else:
        sys.stdout.write(text + "\n")


if __name__ == "__main__":
    main()
