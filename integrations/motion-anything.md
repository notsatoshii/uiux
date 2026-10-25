# motion-anything (motion recipes and the motion standard)

[motion-anything](https://github.com/nexu-io/motion-anything) is a local, zero-dependency motion engine from the Open Design family (`docs/sources.md`): ~400 recipes (kinetic text, ambient CTAs, reveals, sliders, shaders), 59 design-system packs, 58 HyperFrames video templates, and `MOTION-SPEC.md`, a motion standard with duration and easing tokens, a restraint budget per viewport, performance rules and reduced-motion fallbacks. It exports JSON, CSS, React, Lottie, MP4, GIF and portable `SKILL.md` bundles.

## Install

```bash
git clone https://github.com/nexu-io/motion-anything.git <tools>/motion-anything
node <tools>/motion-anything/cli/bin/motion.js serve 4399   # the workbench, optional
```

Node 18+ and nothing else. Its skills (`skills/motion-anything`, `skills/gsap`, `skills/web-to-design-md`, `skills/web-clone`, `skills/web-shader-extractor`) follow the SKILL.md convention: link the ones you want into `~/.claude/skills/` to get `/motion-anything` and `/gsap` in Claude Code.

CLI: `motion list` (recipes), `motion add <recipe-id>` (export a recipe as a portable skill bundle), `motion gallery`, `motion serve [port]`.

## How uiux uses it

- **Critic 07 (motion):** `MOTION-SPEC.md` is the standard for timing, easing, restraint and reduced motion. When the brief is silent, its tokens (`instant` 80–120 ms, `fast` 140–220, `base` 220–320, `slow` 320–500, `deliberate` 500–800; `ease-out` `cubic-bezier(0.16,1,0.3,1)` as the default) replace the ones in `taste/defaults.md`. Its restraint budget is a finding when exceeded: ≤ 1 celebratory moment per viewport, ≤ 3 simultaneous entrances, no competing loops, no auto-played delight.
- **Builder:** for a feedback moment, an entrance, a kinetic-text or an ambient-CTA finding, pick a recipe by id (`motion list`, or the `/motion-anything` router skill), export it (`motion add <id>` or the CSS/React export), and bind it to the project's tokens. One recipe per role on a surface; the same recipe for the same role everywhere.
- **Critic 09 (micro-craft):** recipes composed together must share one easing family and one duration band per role.

## Rules

- Recipes are mechanics. Their demo colours, fonts and copy are not transferred; the project's tokens are.
- Every recipe keeps its `prefers-reduced-motion` fallback (`scale-only`, `crossfade` or `none`).
- Transform and opacity only; nothing that triggers layout.
- A recipe that needs WebGL or a canvas engine is allowed only on persuade and experience surfaces, once per page, with a static poster for reduced motion and for devices that fail the frame budget.
- Record in the cycle report: recipe id, upstream licence (`recipe.motion.yaml > license.upstream`), the token mapping.

## When it is absent

Critic 07 uses `taste/defaults.md`; the builder writes motion by hand under the same rules. Say so in the report's tools line.
