---
name: uiux
description: Autonomous UI/UX design loop. One command interviews you for direction and brand, writes a brief, builds (first time) or takes the existing surface, then runs cycles of parallel critics (best practices, references, design system + tooltips + copy, functionality, aesthetic, visualize, motion, delight) and a single builder until the surface clears a scored bar or plateaus. Use when the user says /uiux, "run the design loop", "loop on this page", or wants a surface built or improved end to end without babysitting.
argument-hint: "<surface path or URL> [--bar 8] [--cycles 6] [--skip-interview] [--only <critic,...>]"
---

# uiux

version: 2.0.0 (2026-10-21) · orchestration checks that the running copy has `loop/direction.md`, `loop/evidence.md` and `taste/calibration.md`

Read [loop/orchestration.md](loop/orchestration.md) before doing anything. It is the whole procedure; this file is the map.

## Phases

1. **Intake** (you, no questions): find the surface, decide new build vs existing, read the project's house rules (`uiux.md` in the project root, then CLAUDE.md), find an existing brief, build the reference board, check the calibration board, and (for an existing surface) build the state harness (`loop/evidence.md`). Facts come from the filesystem, never from the user.
2. **Interview** (`interview/questions.md`): rounds of numbered questions with a recommended answer each, in the style of the `grilling` skill; adjectives are pinned to pictures. Its last design question is the **direction** (`loop/direction.md`): 2–3 working versions of the key screen, side by side with the reference board, and the user picks. Then the definition of done is read back, `docs/design/<surface>/brief.md` is written and the loop starts; no approval step, no question after this. Skipped when a brief exists and the user did not ask for a new one.
3. **First build** (only when the surface does not exist yet): build from the brief and the chosen direction with the project's build-time skills, then the state harness.
4. **Cycles** (`loop/orchestration.md`): evidence pass (every state captured, the task walker runs the usability tasks in a real browser, hard checks) → all nine critics in parallel → merge, cut to 12 findings and one theme → one builder → score → repeat or stop. Three phases: **A structure** (04, 05, 02 lead), **B feel** (06, 07, 08 lead), **C craft** (09, 03, 01 lead). If aesthetic stays at 6 or below twice, the loop reopens direction itself with two structural variants and a judge who has not read the brief. Critics use `tools/` for evidence and `integrations/` when connected.
5. **Report**: `docs/design/<surface>/cycle-N.md` and `evidence/cycle-N.md` per cycle, `final.md` at the end, and a five-line summary in chat.

## Taste

The brief says what the surface is for. Taste says what good looks like, in pictures first: the **calibration board** (`taste/calibration.md`), the owner's approved and rejected screens with their words, which the taste critics, the builder and every judge look at. Then in words, at three levels: the project's `taste.md`, then the owner's taste file (`~/.claude/uiux/taste.md` or `$UIUX_TASTE`, private, across all their projects), then the skill's own `taste/` (curated references, the slop list, known-good defaults), then the installed taste skills, then Mobbin for calibration. Critics 05–09 and the builder load it in that order before they look at the surface (`taste/README.md`).

The owner's file is built by the skill, not typed by hand: `/uiux taste init` seeds it (import what the host knows, then a ten-round pairs interview shown visually); every run appends the owner's reactions to previews, quoted and dated (`taste/owner-taste.md`); `/uiux taste add "<note>"`, `show` and `promote` manage it. If the file does not exist, the first run offers `taste init` once and continues without it.

## Rules that never bend

- Critics read, the builder writes. Never two writers on the same files.
- A critic sees the brief, the screenshots, the code and the previous cycle's screenshots. Never the builder's reasoning or chat.
- Scores need anchors. Every critic rubric in `critics/` carries what a 4, a 7 and a 9 look like. A score without a quoted anchor is invalid; re-run that critic.
- No invented facts: no made-up numbers, claims, curriculum, prices, testimonials. A visual that needs data the project does not have logs `needs data:` instead.
- House rules win over this skill. If `uiux.md` or CLAUDE.md says copy may not change, or text must be in a language and register, every critic and the builder obey it.
- The loop stops on its own: bar reached, plateau, cycle cap or token cap. After the interview it never asks the user anything: not "continue?", not "approve?", not "which option?". When a call is needed (a brand pick, which of two options, a missing asset) it takes the safest option that follows the brief and the design system, logs it as a decision the loop made, and keeps going. Facts, numbers and prices are never invented: they stay as visible `needs data:` placeholders. Copy under a "copy may not change" rule stays unchanged; proposed rewrites are listed. Both are reviewed in `final.md` after the run.
- Report faithfully. A failed check is reported as failed, with the evidence.

## Subcommands

- `/uiux taste init` seed the owner's taste file (import + pairs interview).
- `/uiux taste add "<note>"` append a line. `/uiux taste show` print it. `/uiux taste promote` move repeated lines to Standing rules.
- `/uiux taste add-shot <image> approved|rejected "<words>"` add a screen to the calibration board.

## Flags

- `--bar N` the score every critic must reach (default 8, see house rules).
- `--cycles N` hard cap on cycles (default 6).
- `--skip-interview` use the existing brief without the "anything changed?" question.
- `--only a,b` run only the named critics (ids in `critics/`), for a focused pass.
- `--dry` run intake and interview, write the brief, stop before any build.
