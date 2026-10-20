# 07 Motion

Two checks, one score (the lower, then adjust by one at most). Runs only once functionality holds ≥ 8. From the cycle after critic 06 first ran, check B also covers the visuals it introduced.

## Check A: entrance and data motion

What moves when the page loads and as the visitor scrolls, and does it explain anything?

- Entrance: sections reveal on first view with a short, eased fade or rise; staggered for grids; nothing re-animates on scroll-back.
- Data: stat tiles count up, bars grow, lines trace, sparklines sweep, flows reveal one node at a time, before/after crossfades or slides; the motion matches the meaning (growth grows, steps step).
- Timing: 300–800 ms, ease-out or spring; nothing loops; nothing bounces unless the brief's words ask for playful.
- Reading first: nothing the visitor needs to read right now is still moving; count-ups finish before adjacent text appears.
- Reduced motion: a static version exists and is used when `prefers-reduced-motion` is set.
- Cost: animations on transform and opacity only; no layout thrash; no jank on the phone viewport.

## Check B: interaction feedback

Every element the visitor can touch answers, consistently.

- Hover: buttons lift or deepen; cards respond (tilt, glow, border); links underline-slide; images zoom a hair; icons nudge. Under 150 ms.
- Press: scale-down or colour snap on active, then settle. Under 100 ms.
- Focus: a visible ring in the brand's colour, never the browser default, on every focusable element.
- State changes: toggles, tabs, accordions, menus, modals animate between states instead of jumping; the direction of the motion matches the spatial model (a drawer slides from where it lives).
- Feedback moments: success check, copied tick, field valid/invalid, loading spinner or skeleton, disabled look.
- Touch: hover effects never stick on touch devices (`@media (hover: hover)` or equivalent); the press effect is the touch feedback.
- Cursor: pointer on everything clickable; a custom cursor only if the brief asks.
- One system: all buttons of a kind share the same hover and press; all cards share theirs. A lone element that behaves differently is a finding.

## Anchors

- **4:** no entrance motion or a looping, bouncing one; stat numbers sit static; hover and press feedback missing on main actions, or the browser default focus ring; hover states stick on the phone screenshot.
- **7:** entrance and data motion exist and are eased; buttons answer on hover and press; focus ring is branded; one gap (a chart that pops instead of drawing, a modal that jumps, a card that ignores hover, reduced motion unhandled).
- **9:** motion explains the data and you would miss it if it were gone; every interactive element answers on hover, press and focus, consistently, within the timing limits; a phone user never sees a stuck hover; reduced motion gives a complete static page.
