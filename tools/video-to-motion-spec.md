# Video to motion spec

The user records a short clip (5–15 s) of an interaction they like, anywhere: a product, a site, a prototype. Instead of describing it in words (lossy), extract its timing and turn it into a spec the builder can implement and critic 07 can check.

## Steps

1. `python tools/frames.py clip.mp4 --fps 24 --out docs/design/<surface>/motion-ref/<name>/` writes numbered frames and `timeline.json` (per-frame mean absolute pixel change, 0–1).
2. Read `timeline.json`. Each motion is a bump: it starts where change rises above the noise floor, peaks, and settles where change returns to the floor. Note start, peak and end times for each bump. Several overlapping bumps are a stagger.
3. Open the frames at the start, the peak and the end of each bump. Describe what moved: which element, from where to where (translate, scale, opacity, colour, blur), and in what order relative to other elements.
4. Fit the easing: change rising fast then slowing = ease-out; slow then fast = ease-in; a small reversal after the peak = overshoot (spring). Report duration = end − start.
5. Write the spec (below). Only the mechanics are transferred: timing, easing, order, direction. The reference's look (colours, shapes, copy) is not part of the spec.

## Spec format

```
motion: <name>            source: <clip path> (mechanics only)
trigger: <scroll into view | hover | press | load | state change>
sequence:
  1. <element role>: <property> from <a> to <b>, start 0 ms, duration 420 ms, ease-out
  2. <element role>: opacity 0→1, start 120 ms (stagger +60 ms per item), duration 300 ms, ease-out
settle: everything at rest by <N> ms
reduced motion: <what shows instead>
notes: <what made it feel right: e.g. the text waits until the number finishes>
```

The builder implements it with the project's motion tools (CSS transitions, the project's spring library, GSAP if present). Critic 07 compares the result's timeline (run `frames.py` on a screen recording of the built page) with the spec's numbers; a deviation over 25 % in duration or a different easing shape is a finding.
