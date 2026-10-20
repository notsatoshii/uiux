# 03 Design system, tooltips and copy clarity

Three scans, one score (the lowest of the three, then adjust by one at most).

## Scan A: system consistency

- Tokens: colours, spacing, radii, shadows, type sizes come from one set (CSS variables, Tailwind config, DESIGN.md). Count one-off values in the surface's CSS; each cluster is a finding.
- Type scale: at most 5–6 sizes in use, a clear hierarchy, consistent line-height per size, consistent weights for the same role.
- Spacing rhythm: one scale (4/8-based or the project's); section gaps consistent; card paddings consistent.
- Components: every button looks like a button of its kind (primary, secondary, ghost) everywhere; every card, input, badge likewise. A lone element styled differently from its siblings is a finding.
- Dark mode (if the brief requires it): tokens redefined, no hard-coded light colours, images and shadows still read.

## Scan B: tooltip need

Where does the visitor need help in place, and is it there?

Need a tooltip or inline help, flag if missing:
- icon-only buttons (also need an accessible name)
- jargon, abbreviations, metric names, internal codes
- form fields whose right answer is not obvious
- disabled controls (say why)
- truncated text (the full value)
- numbers that need context (period, unit, exclusions)
- chart data points (hover/tap value)

Flag the opposite too:
- tooltips on things already clear: remove
- essential information living only in a tooltip: move it onto the page; the brief's phone users do not hover
- tooltips that fail the house copy rules (language, register)

Every tooltip must be reachable on touch (tap) and keyboard (focus) and be announced to screen readers.

## Scan C: copy clarity

Not copywriting; clarity. Labels say what happens ("Save and continue", not "Submit"); error messages say what to do; empty states say what will appear and how to start; buttons are verbs; nothing requires the visitor to guess. Copy obeys the house rules (language, register, forbidden words). When the house rules say copy may not change, clarity findings go to `waiting_on_user`, not findings.

## Anchors

- **4:** several one-off values per screen, two button styles for the same role, icon buttons with no help, a label like "Submit" or "OK" on the main action, or an essential explanation only in a tooltip.
- **7:** tokens are used almost everywhere; one or two stray values; every icon control has a name; jargon mostly explained; one label still vague.
- **9:** nothing on the surface is styled outside the system; the system itself is small; every ambiguous element has help in place, nothing essential hides in a tooltip, and a phone user loses nothing; every label tells the visitor what will happen.
