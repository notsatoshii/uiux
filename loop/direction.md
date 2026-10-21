# Direction

The loop's critics find faults and the builder patches them. That cannot fix a wrong direction: in the first two real runs the aesthetic score sat at 6–7 for every cycle while the real problem ("the same white rounded card on a cream ground", "green and gold shapes everywhere") stayed. Direction is chosen before the cycles, by the owner, from pictures, and reopened by the loop when it stalls.

## When

- **Before cycle 1**, after the interview's rounds 1–3 and before the brief is written: always for a new surface or a redesign; skipped for a narrow fix (`--only`, or the user said "keep the look").
- **Reopened by the loop** when the aesthetic score (05) is 6 or less two cycles in a row, or the fresh-eyes check fails twice. No question to the owner then; see "Reopen" below.

## Make the directions (2 or 3)

1. **Pick the key screen.** The one screen that carries the one job (the home of an app, the hero and first fold of a landing page, the report of a tool). Directions are made for that screen only, at the primary viewport.
2. **Ground each direction.** Each direction is one coherent visual world, written in five lines before it is built: ground and ink colours, one accent and where it is used, type pairing and the heading weight, density, the one signature element. Each must agree with the reference board's proportions (orchestration intake 5c), pass `taste/slop.md`, and respect the owner's calibration board (`taste/calibration.md`): nothing that resembles a rejected screen.
3. **Make them different.** Directions differ in world, not in detail: e.g. one quiet and editorial, one dense and tool-like, one with a single strong signature element. Two directions that a stranger would call "the same with a different colour" do not count; replace one.
4. **Respect what is fixed.** Copy, features, the logo, the owner's assets and the house rules are the same in every direction. A redesign keeps the real content of the screen; no lorem, no invented numbers.
5. **Build them cheaply and for real.** Each direction is a working static version of the key screen, built in the project's stack behind a flag or a preview route (`?direction=a`, `/__direction/a`), or as one self-contained HTML file in the scratchpad when the stack makes that slow. Same content, real fonts, real tokens. Not a mood board, not a description.
6. **Screenshot** each at the primary viewport (and one at desktop if the surface is desktop-first).

## Show them

One image: the directions side by side at the same scale, each labelled A / B / C with its five-line description underneath, and the reference board as a strip below. Send it to the owner (in the chat, and with SendUserFile when the owner follows from another device).

This is the last interview question: "Which direction, and what would you change in it?" with a recommended pick and why. The owner may pick one, combine ("A's type with B's density"), or reject all; on reject-all, read their words, write two new directions from them, show again (at most twice, then take the owner's closest pick).

Record in the brief: the chosen direction's five lines, the owner's words, the rejected directions and why (their words). The owner's reaction also goes to the taste file (3.6) and the chosen and rejected screenshots to the calibration board (`taste/calibration.md`).

## Build from it

The first build (or, for an existing surface, cycle 1's builder) applies the chosen direction to every screen in scope, starting from the key screen. Remove the direction flag and the unchosen variants before cycle 1's screenshots.

## Reopen (no owner question)

When aesthetic ≤ 6 twice in a row, or the fresh-eyes check fails twice:

1. The orchestrator writes a one-paragraph diagnosis: what the critics and the fresh-eyes agent keep naming, against the reference board and the calibration board.
2. The builder makes two structural variants of the key screen that answer the diagnosis (layout, hierarchy, density, type weight: not colour tweaks).
3. A judge subagent that has not read the brief sees the current screen and the two variants next to the reference board and the calibration board, and picks one (or "current"), with one sentence why.
4. If a variant wins, the next cycle's builder rolls it out to all screens (a structural cycle; the 12-finding cap does not apply to the roll-out). Log the reopen and the pick under "decisions the loop made".
5. At most two reopens per run.
