# uiux

An autonomous UI/UX design loop for [Claude Code](https://claude.com/claude-code). One command interviews you for direction and brand, writes a brief, builds the surface (first time) or takes the one you have, then runs cycles of parallel critics and a single builder until the page clears a scored bar or stops improving.

```
/uiux src/app/page.tsx
/uiux https://localhost:3000/pricing --bar 9
/uiux site/src/pages/index.astro --skip-interview --only 05-aesthetic,07-motion
```

## Why

Asked for a page, a model gives you the statistical average of the web: a cream hero, three cards, a gradient. It looks done in ninety seconds and nobody checks whether it is good. uiux separates the two problems:

1. **Direction before pixels.** A short interview (purpose, audience, three words and three anti-words, references as mechanics not looks, a signature move, what may never be invented) becomes a written brief that every later step is held to.
2. **Critics, then one builder, in a loop.** Each cycle, eight critics read the brief, the screenshots and the code in parallel and score against written anchors. One builder fixes the ranked list. Screenshots again, score again, until the bar is met, the scores plateau, or a cap is hit. It does not ask "continue?".

## The critics

| id | lens |
|---|---|
| 01 best practices | semantics, accessibility, responsive, performance, robustness |
| 02 references | mechanics from the brief's references, never their look; conversion patterns that fit the job |
| 03 design system | tokens and consistency · tooltip need (and tooltip excess) · copy clarity |
| 04 functionality | every feature works, every task completes, every state exists; gates the next four |
| 05 aesthetic | the brand's three words, the logo test, hierarchy, no default tropes |
| 06 visualize | text and numbers that should be visuals; visuals that earn their place; no invented data |
| 07 motion | A: entrance and data motion · B: hover, press, focus, state-change feedback; touch-safe |
| 08 delight | the signature move, personality, craft one level deeper; plus an ideas list that is never auto-built |

Every rubric carries three anchors (what a 4, a 7 and a 9 look like). A score must quote the anchor it used, or it is thrown out. From cycle 2, each critic first compares the new screenshots to the previous cycle's blind, before reading the new code.

## Stop rules

- **Bar:** every active critic ≥ bar (default 8) and no severity-1 finding open.
- **Plateau:** most critics say "same" or "worse" two cycles running.
- **Cap:** `--cycles` (default 6) or a token budget from the house rules.
- **User's call:** the only open blockers need the user (copy, brand, facts, money).

## House rules

Put a `uiux.md` in your project root to set rules the loop obeys above its own: copy language and register, "copy may not change", feature parity on redesigns, forbidden words, default bar, token budget. The loop also reads your `CLAUDE.md`. See [examples/uiux.md](examples/uiux.md).

## Install

```bash
git clone https://github.com/notsatoshii/uiux ~/.claude/skills/uiux
```

Or clone anywhere and symlink the folder into `~/.claude/skills/`. The loop uses whatever is installed: the `grilling` skill's round format for the interview (falls back to its own), `impeccable` or `design-taste-frontend` for building, a browser or Playwright tool for screenshots (falls back to code-only review and says so).

## Layout

```
SKILL.md                  the command: phases, rules, flags
loop/orchestration.md     the procedure the main session follows
interview/questions.md    the question bank, in rounds
interview/brief-template.md
critics/00-shared.md      what every critic gets, the output JSON, severity rules
critics/01..08-*.md       one lens each, with anchors
builder/fix.md            the single writer's rules
templates/cycle-report.md
examples/uiux.md        a house-rules file
```

## What it is not

Not a design system, not a component library, not a replacement for taste. It is a procedure that makes a model ask before it builds, check after it builds, and stop when it is done.

MIT.
