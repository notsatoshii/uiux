# Interview question bank

Run with the `grilling` skill's round format: a round is every question whose prerequisites are settled, numbered, each with a recommended answer. Wait for answers, recompute, next round. Skip anything already answered by the brief, house rules, PRODUCT.md or DESIGN.md. Facts (what framework, what exists, what the current page looks like) are yours to look up, never the user's to type.

Keep the whole interview under four rounds for a single page. The user is giving direction, not writing a spec.

## Round 1: purpose

1. **The one job.** When this surface works, what did the visitor just do? One action (sign up, buy, finish the task, understand X). If two compete, which wins?
2. **Who, on what.** Who is the visitor (role, context, mood when they arrive) and what device, mostly? Recommend from the project's existing audience if known.
3. **New or existing.** Confirm the intake finding. For an existing surface: what must not change (features, copy, routes, data)?
4. **Mode.** Persuade, operate, read or experience. Recommend from the surface type.

## Round 2: brand point of view

5. **Three words, three anti-words.** Three adjectives the surface should feel like and three it must never feel like. Recommend a set from existing brand material if any.
6. **Core belief.** The one sentence the visitor should still believe after leaving. (The Scrollcraft "core belief statement".)
7. **References, with the rule.** Two or three products or pages whose *mechanics* to learn from (pricing toggle, onboarding order, how they show proof). State back the rule: take mechanics, never visuals; no 1:1 clones. When Appshots or Mobbin is connected, search first and suggest: 3–5 candidate apps, each with the one mechanic worth taking and 1–2 screenshots; the user confirms, removes or adds, and only confirmed apps enter the brief (see `integrations/appshots.md`).
8. **Visual world.** Existing tokens, fonts, palette, DESIGN.md? If yes: keep, expand, or replace. If none: pick a direction now (recommend one, name the fonts and the palette feel) so the critics have something to hold the build to. If the user hands you a reference image for the feel, run `tools/extract-tokens.py` on it and put the measurements (contrast, whitespace ratio, spacing unit) in the brief; the colours themselves are not transferred.
9. **Signature move.** One memorable interaction or moment unique to this surface. Recommend one. "None" is an acceptable answer for operate-mode surfaces. If the user has a clip of an interaction they like, run `tools/video-to-motion-spec.md` on it and attach the spec to the brief.
9b. **Appshots or Mobbin, when connected.** For the surface type and each reference, search flows and sections once and show two or three candidate mechanics with their screen ids; the user picks. See `integrations/appshots.md` and `integrations/mobbin.md`.

## Round 3: content and proof

10. **Real assets.** What exists: photos, logos, screenshots, data, testimonials, numbers. What is missing and may be generated (illustration, placeholder), and what may never be invented (numbers, quotes, prices, facts).
11. **Copy rules.** Language, register (e.g. Korean 존댓말), forbidden words, whether copy may change at all. Pulled from house rules if present; confirm.
12. **Proof.** What evidence can the page show for its claims, and where does it come from?
13. **Scroll journey.** Section by section from the top: what the visitor sees, what reveals or moves there, loud or quiet, and what they should believe by the end of it. Recommend the whole map in one block; the user edits. This becomes the brief's scroll journey, which the motion critic checks against. For operate surfaces this is the task path instead of a scroll.
13b. **Receipts.** For every claim or number the page will make: where is the evidence, and will the page show it (footnote, source drawer, live number, screenshot)? A claim with no receipt is cut or rewritten as a range; nothing is invented.

## Round 4: features and the bar

14. **Feature list.** For an operate surface: every task the user must be able to do here. For persuade: every section, in order. This list becomes the functionality critic's checklist.
15. **Accessibility and devices.** Minimum viewports, dark mode, reduced motion, keyboard users, screen readers: which are required, which nice to have.
16. **Bar and budget.** Score bar (default 8; 9 for flagship, 7 for internal), cycle cap (default 6), token or time budget if any.
17. **Definition of done.** Read back: the one job, the three words, the must-not-change list, the feature list, the bar. Ask for approval. On approval, write the brief.

## Redesign branch

When the surface exists, add to round 1:

- R1. **Parity.** Every feature the current surface has, listed from the code (you list it, the user confirms). All of it stays unless named here.
- R2. **Usability tasks.** Three tasks a real user does on this surface today, used as the functionality critic's walk-through.
- R3. **What is wrong.** The user's own view of what fails today, in their words. This seeds, not replaces, the critics.
