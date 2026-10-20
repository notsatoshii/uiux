#!/usr/bin/env python3
"""Split a screen recording into frames and a motion timeline (FFmpeg + Pillow).

Usage: python frames.py <video> [--fps 12] [--out frames/]

Writes frame-0001.png … and timeline.json: for each frame, the time in ms and the mean absolute
pixel change from the previous frame (0–1), plus the detected motion bumps (start, peak, end,
duration) so a critic can read timing and easing. See video-to-motion-spec.md.
"""
import argparse
import json
import os
import subprocess
import sys

from PIL import Image, ImageChops, ImageStat


def extract(video, fps, out):
    os.makedirs(out, exist_ok=True)
    cmd = ["ffmpeg", "-loglevel", "error", "-y", "-i", video, "-vf", f"fps={fps},scale=320:-1", os.path.join(out, "frame-%04d.png")]
    subprocess.run(cmd, check=True)
    return sorted(f for f in os.listdir(out) if f.startswith("frame-") and f.endswith(".png"))


def changes(out, files):
    prev = None
    rows = []
    for f in files:
        im = Image.open(os.path.join(out, f)).convert("L")
        if prev is not None:
            diff = ImageChops.difference(im, prev)
            rows.append(ImageStat.Stat(diff).mean[0] / 255.0)
        else:
            rows.append(0.0)
        prev = im
    return rows


def bumps(rows, fps, floor_ratio=0.15):
    if not rows:
        return []
    peak_all = max(rows) or 1.0
    floor = max(0.004, peak_all * floor_ratio)
    out, start = [], None
    for i, v in enumerate(rows):
        if v > floor and start is None:
            start = i
        elif v <= floor and start is not None:
            seg = rows[start:i]
            p = start + seg.index(max(seg))
            out.append({"start_ms": int(start * 1000 / fps), "peak_ms": int(p * 1000 / fps), "end_ms": int(i * 1000 / fps),
                        "duration_ms": int((i - start) * 1000 / fps), "peak_change": round(max(seg), 4),
                        "shape": "ease-out" if (p - start) <= (i - p) else "ease-in"})
            start = None
    if start is not None:
        out.append({"start_ms": int(start * 1000 / fps), "end_ms": int(len(rows) * 1000 / fps), "open": True})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--fps", type=int, default=12)
    ap.add_argument("--out", default="frames")
    a = ap.parse_args()
    files = extract(a.video, a.fps, a.out)
    rows = changes(a.out, files)
    timeline = {"source": a.video, "fps": a.fps, "frames": len(files),
                "change": [{"frame": f, "ms": int(i * 1000 / a.fps), "delta": round(v, 4)} for i, (f, v) in enumerate(zip(files, rows))],
                "bumps": bumps(rows, a.fps)}
    with open(os.path.join(a.out, "timeline.json"), "w", encoding="utf-8") as fh:
        json.dump(timeline, fh, indent=1)
    sys.stdout.write(json.dumps({"frames": len(files), "out": a.out, "bumps": timeline["bumps"]}, indent=1) + "\n")


if __name__ == "__main__":
    main()
