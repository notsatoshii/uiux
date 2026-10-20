# 01 Best practices

Lens: does the surface meet the web's baseline for accessibility, responsiveness, performance and semantics? Nothing about taste here.

## Checks

- **Semantics:** one h1, heading order, landmarks (header/nav/main/footer), lists are lists, buttons are buttons (not divs with handlers), links go somewhere.
- **Accessibility:** text contrast ≥ 4.5:1 (3:1 for large text and UI parts), every image has alt or is marked decorative, every icon-only control has an accessible name, focus visible and in order, no keyboard traps, form fields labelled, errors announced, `prefers-reduced-motion` respected.
- **Responsive:** no horizontal scroll at the smallest brief viewport, 16px side gutters on phones, tap targets ≥ 44px, text never under 14px on phones, layout holds at 200% zoom.
- **Performance:** images sized and lazy where off-screen, fonts limited and preloaded or swapped, no layout shift on load (reserve space for images, fonts, embeds), no blocking scripts in head, animations on transform/opacity only.
- **Robustness:** long text, empty data, slow network, missing image: does the layout survive? Loading, empty and error states exist where data loads.
- **Hygiene:** no console errors, no broken links, viewport meta present, lang attribute set, title present.

## Anchors

- **4:** at least one of: contrast failures on body text, horizontal scroll on phone, icon buttons with no name, h1 missing or several, console errors. The page works for a mouse user on a laptop and few others.
- **7:** semantics and contrast pass; focus is visible; phone layout holds; one or two gaps remain (a missing empty state, a late-loading image shifting the page, reduced motion not handled).
- **9:** a keyboard-only user and a screen-reader user can do the one job; nothing shifts on load; every state (loading, empty, error, long text) has been seen in a screenshot and holds; no console noise.
