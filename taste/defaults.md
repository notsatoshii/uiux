# Known-good defaults

For when the brief is silent. The project's tokens and `taste.md` win over all of this. These are starting points that do not look like a template; they still need the brief's three words to become a design.

## Type

- Two faces at most: one display (with character; one or two weights) and one text (wide family, excellent at 15–17px). Pairings that hold: a grotesk display with a humanist text; a serif display with a grotesk text; one superfamily used at two optical sizes.
- Korean: Pretendard for text; a display face with real Hangul coverage (not a Latin face with fallback). `word-break: keep-all`, `line-height` 1.6–1.7 for body, 1.2–1.3 for display. Subset the display face if it is only used for headings.
- Scale: pick a ratio (1.2 for operate, 1.25–1.333 for persuade) and a base (15 or 16px). Five or six steps. Hierarchy by weight and colour before size: a 600 heading in ink next to 400 body in secondary grey reads better than a bigger heading.
- Measure: 45–75 characters per line (Korean: about 35–45 characters). Headings tight-tracked only at display sizes; body at 0.
- Numbers: tabular figures in tables and stat tiles.

## Spacing

- One scale: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128. Section gaps from the top half of the scale; component padding from the bottom half.
- Sections are not all the same height. Vary density on purpose: a tight proof strip after a tall hero; a wide quiet reading block before a dense comparison.
- Phone: 16–20px side gutters, 44px minimum tap targets, 12–16px between stacked tap targets.
- Optical, not mathematical: a bigger element needs a bigger gap; icons sit on the text's x-height, not the line box.

## Colour

- Ground (not white: a tinted near-white, or a tinted near-black), ink (not black: a tinted dark), secondary text at 7:1 or better on the ground, one accent, one or two supporting tints for backgrounds of sections.
- The accent means "act": buttons and the key link. It is not used for decoration, headings or icons at large.
- Section backgrounds change by tint, not by hue, except once for the loud zone.
- Dark mode is its own set of tokens, with surfaces at two or three elevations; shadows mostly replaced by borders and lighter surfaces.

## Shadows and surfaces

- Shadow colour = ink or accent at low alpha, never neutral black. Two or three sizes, named: `sm` for hover lifts, `md` for cards, `lg` for modals and the floating thing in the hero.
- One light direction for the whole page (top-left by default); clay and 3D assets must match it.
- Borders: a 1px hairline at ink/12 % on light, white/10 % on dark. Border or shadow, not both for the same job.
- Radius family: 4 / 8 / 12 / 16 / 24 (or the project's); nested elements use outer − padding.

## Motion

- Durations: 120 ms for hover and press feedback, 200–300 ms for state changes (toggles, tabs, menus), 300–500 ms for entrances, up to 800 ms for one hero moment. Nothing on a product page loops.
- Easing: ease-out for anything entering (fast then settle), ease-in-out for anything moving between two places, a spring with low bounce for feedback on a playful brand, none for a serious one.
- Stagger: 40–80 ms between items in a group; cap the group at six so the last item is not waiting.
- Entrance: translate 8–16px and opacity 0→1; never scale from 0; never blur.
- Scroll-triggered motion fires once, at 20–30 % visibility; it is off under `prefers-reduced-motion`.
- Hover effects behind `@media (hover: hover)`; press feedback is the touch feedback.

## Buttons and controls

- Primary: filled accent, white text at 4.5:1, radius from the family, 44px tall on phone, label is a verb with its object ("진단 시작하기", "Save and continue").
- Secondary: ink outline or tinted ground, same height and radius.
- One primary per viewport. If there are two, the second is secondary.
- Focus ring: 2px, accent or ink, offset 2px, on every focusable element.

## Imagery

- Real screenshots of the real product, current, at 2×, with real data or clearly labelled sample data.
- Illustrations and 3D in one world: one light, one material language, one palette.
- Photos with one treatment (crop ratio, tone), or none. No stock.
- Charts follow the project's dataviz rules; otherwise one series colour = accent, the rest in tints of ink.
