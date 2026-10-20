# 09 Micro-craft (the "Pepsi-bubbling" pass)

Lens: one level deeper than the visitor consciously notices. Runs only in a cycle where every other active critic scored ≥ bar − 1, so it polishes a surface that already works. It produces a numbered checklist, not a score argument: the reference's origin is a 17-point list made in a critique of one small graphic.

## Method

Take the two most important screenshots (hero at the phone viewport, the ask at the desktop viewport). Zoom. For each, write a numbered list of every detail that is a little off. Expect 10–20 items on a first pass; fewer than 5 means you did not zoom.

## What to check

- **Radii:** one family (e.g. 12/22/32). Nested radii: inner = outer − padding. Pills are fully round, not "almost".
- **Shadows:** tinted with the surface's ink or accent, never neutral grey; softer and larger for higher elevation; one direction of light across the whole page.
- **Gradients and washes:** no banding; stops that make sense; the hero wash does not fight the text.
- **Borders:** one hairline weight and one colour at a given opacity; never a border and a shadow doing the same job.
- **Icons:** one stroke weight, matched to the type's weight; optically centred in their containers; same size family; same corner style as the type (rounded type → rounded icons).
- **Type:** optical alignment of headings to the grid edge (the first letter's side bearing); tight tracking on display sizes; consistent line-length; no orphans in headings; hanging punctuation where the typeface allows; Korean `word-break: keep-all`.
- **Alignment:** baselines across columns; icon centre to text x-height; button label optically centred (cap height, not box height); number columns right-aligned.
- **Spacing:** equal optical, not equal mathematical, gaps around elements of different visual weight; consistent internal padding ratio in cards and buttons.
- **Images and 3D:** matched light direction with the page's shadows; consistent crop and scale; edge halos removed; sharp at 2× density.
- **Motion physics (if critic 07 ran):** matched easing curves across similar elements; no two things of the same kind with different durations; overshoot only where the brand's words allow it.
- **Colour:** the same semantic colour everywhere it means the same thing; accents not overused (count them per screen); text on tinted backgrounds re-checked for contrast.
- **States:** hover and focus rings share the radius of the element; disabled state is one treatment everywhere.

## Output

The shared JSON, with each list item as a severity-3 finding and the element pinned (screenshot + position or selector). Score:

- **4:** more than 20 items, including shadows in grey, mixed radii, icons heavier than the type.
- **7:** 8–15 items, none of them systemic; the light direction and radius family hold.
- **9:** under 5 items, each a judgement call; nothing a designer would redo.
