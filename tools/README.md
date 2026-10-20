# Tools

Small scripts the critics and the interview use for evidence instead of opinion. All need Python 3.10+ with Pillow (`pip install pillow`), nothing else. `frames.py` also needs FFmpeg on the PATH.

| script | used by | input → output |
|---|---|---|
| `extract-tokens.py <image> [--out tokens.json]` | interview Q8 (visual world) | a reference image → JSON of dominant colours (hex, share, role guess), background vs ink contrast, estimated base spacing unit and whitespace ratio |
| `sightline.py <screenshot> [--out map.png]` | critic 05 (aesthetic) | a screenshot → a blurred luminance-contrast map with the three strongest attention regions boxed and listed (x, y, w, h, weight), top to bottom |
| `frames.py <video> [--fps 12] [--out frames/]` | video-to-motion-spec (`video-to-motion-spec.md`) | a screen recording → numbered frames plus a `timeline.json` of per-frame mean pixel change, so the critic can read start, peak and settle of each motion |

Run from anywhere: `python <skill-dir>/tools/sightline.py docs/design/home/shots/cycle-1/mobile-hero.png`.

These are helpers. A critic still looks at the image; the script gives it numbers to point at.
