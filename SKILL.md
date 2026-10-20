---
name: uiux
description: Autonomous UI/UX design loop. One command interviews you for direction and brand, writes a brief, builds (first time) or takes the existing surface, then runs cycles of parallel critics (best practices, references, design system + tooltips + copy, functionality, aesthetic, visualize, motion, delight) and a single builder until the surface clears a scored bar or plateaus. Use when the user says /uiux, "run the design loop", "loop on this page", or wants a surface built or improved end to end without babysitting.
argument-hint: "<surface path or URL> [--bar 8] [--cycles 6] [--skip-interview] [--only <critic,...>]"
---

# uiux

Read [loop/orchestration.md](loop/orchestration.md) before doing anything. It is the whole procedure; this file is the map.

## Phases

1. **Intake** (you, no questions): find the surface, decide new build vs existing, read the project's house rules (`uiux.md` in the project root, then CLAUDE.md), find an existing brief. Facts come from the filesystem, never from the user.
2. **Interview** (`interview/questions.md`): rounds of numbered questions with a recommended answer each, in the style of the `grilling` skill. Ends with a definition of done the user approves. Output: `docs/design/<surface>/brief.md` from `interview/brief-template.md`. Skipped when a brief exists and the user did not ask for a new one; then ask one question: "Anything changed since this brief?"
3. **First build** (only when the surface does not exist yet): build from the brief with the project's build-time skills (`impeccable`, `design-taste-frontend` or whatever is installed), then screenshot.
4. **Cycles** (`loop/orchestration.md`): parallel critics → merged ranked findings → one builder → screenshots → score → repeat or stop. Nine critics in `critics/`, gated by progress: 01–05 always; 06 visualize, 07 motion, 08 delight once functionality holds ≥ 8; 09 micro-craft once everything else is within one point of the bar. Critics use the scripts in `tools/` for evidence and the connectors in `integrations/` (Mobbin, HyperFrames or Remotion, Lottie) when present.
5. **Report**: `docs/design/<surface>/cycle-N.md` per cycle, `docs/design/<surface>/final.md` at the end, and a five-line summary in chat.

## Taste

The brief says what the surface is for. Taste says what good looks like, at three levels: the project's `taste.md`, then the owner's taste file (`~/.claude/uiux/taste.md` or `$UIUX_TASTE`, private, across all their projects), then the skill's own `taste/` (curated references, the slop list, known-good defaults), then the installed taste skills, then Mobbin for calibration. Critics 05–09 and the builder load it in that order before they look at the surface (`taste/README.md`).

The owner's file is built by the skill, not typed by hand: `/uiux taste init` seeds it (import what the host knows, then a ten-round pairs interview shown visually); every run appends the owner's reactions to previews, quoted and dated (`taste/owner-taste.md`); `/uiux taste add "<note>"`, `show` and `promote` manage it. If the file does not exist, the first run offers `taste init` once and continues without it.

## Rules that never bend

- Critics read, the builder writes. Never two writers on the same files.
- A critic sees the brief, the screenshots, the code and the previous cycle's screenshots. Never the builder's reasoning or chat.
- Scores need anchors. Every critic rubric in `critics/` carries what a 4, a 7 and a 9 look like. A score without a quoted anchor is invalid; re-run that critic.
- No invented facts: no made-up numbers, claims, curriculum, prices, testimonials. A visual that needs data the project does not have logs `needs data:` instead.
- House rules win over this skill. If `uiux.md` or CLAUDE.md says copy may not change, or text must be in a language and register, every critic and the builder obey it.
- The loop stops on its own: bar reached, plateau, cycle cap or token cap. It never asks "continue?" mid-loop. It does stop for the user's own calls: copy, brand picks, money, facts.
- Report faithfully. A failed check is reported as failed, with the evidence.

## Subcommands

- `/uiux taste init` seed the owner's taste file (import + pairs interview).
- `/uiux taste add "<note>"` append a line. `/uiux taste show` print it. `/uiux taste promote` move repeated lines to Standing rules.

## Flags

- `--bar N` the score every critic must reach (default 8, see house rules).
- `--cycles N` hard cap on cycles (default 6).
- `--skip-interview` use the existing brief without the "anything changed?" question.
- `--only a,b` run only the named critics (ids in `critics/`), for a focused pass.
- `--dry` run intake and interview, write the brief, stop before any build.
