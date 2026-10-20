# Taste

The brief says what the surface is for and how the brand feels. It does not say what good looks like. This folder does. Every critic in 05–09 and the builder load it before they look at the surface, in this order; the earlier item wins where two disagree.

1. **The project's `taste.md`** (project root, see `examples/taste.md`): what the owner likes and hates, with examples. Wins over everything below. Absent → skip.
2. **House rules** (`uiux.md`, CLAUDE.md): rules, not taste, but they bound it.
3. **`references.md`** here: curated products and pages by mode, each with why it is good. Use them as a bar, never as a layout to copy.
4. **`slop.md`** here: the tells of AI-default design. Each present without a reason in the brief is an automatic finding.
5. **`defaults.md`** here: known-good type, spacing, motion, shadow and colour choices for when the brief is silent.
6. **Installed taste skills**, when present in `~/.claude/skills/`: `impeccable` (read `reference/craft-floor.md`), `design-taste-frontend`, `high-end-visual-design`. Read the parts that apply to the surface's mode. These are the deepest sources; `references.md` and `defaults.md` are the short form for when they are not installed.
7. **Mobbin**, when connected: for the surface type, look at the top screens to calibrate density, hierarchy and section order for this kind of page. Mechanics and calibration only; a layout recognisable from a Mobbin screen is a finding.

## The test taste must pass

A surface that follows the brief and has no slop can still be dull. The aesthetic critic's 9 anchor ("a designer would ask who made it") is the taste bar. To reach it the critic names, in its summary, which reference in `references.md` or `taste.md` the surface comes closest to, and what the gap is. "Closest to nothing in particular" is a finding in itself.

## Keeping taste honest

- Taste never overrides the brief's three words or the house rules. If the owner's `taste.md` wants loud and the brief says quiet for a section, the brief wins for that section and the critic says so.
- Taste never invents facts, copy or data.
- Taste is not a trend. `references.md` lists work that has held up for years, not this month's gallery.
