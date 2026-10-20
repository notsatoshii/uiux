# Generated motion assets: HyperFrames and Remotion

When the brief lists an asset gap that *may be generated* and the asset is motion (an explainer loop, an animated diagram, a product-flow clip, a hero background, an animated chart for a section that cannot be live), the builder makes it from code rather than from an image model. Code assets stay on-brand by construction: they use the project's tokens and fonts, and they can be regenerated when copy or data changes.

Two engines; pick by what is installed:

| | HyperFrames | Remotion |
|---|---|---|
| What it is | HTML + CSS + GSAP compositions rendered to video; built for coding agents | React components rendered frame by frame to video |
| In Claude | connector **HyperFrames by HeyGen** (`compose`, `render_video`); or the skills `npx skills add heygen-com/hyperframes` giving `/hyperframes`, `/hyperframes-cli`, `/gsap` | official agent skills from remotion.dev (`/remotion-*`), installed per the current docs at remotion.dev/docs/ai |
| Needs | Node 22+, FFmpeg for local render | Node, a Remotion project (`npx create-video@latest`) |
| Best for | marketing clips, animated slides, scroll-sequence previews, anything HTML can draw | data-driven video, when the project is already React and the asset should share its components |

Default: HyperFrames for the Astro site, Remotion for the Next app. Either is fine; do not install both for one asset.

## Rules

- The asset is specified first, in the cycle report, as: purpose, where it sits, duration, what it shows, the data it uses (source named), the tokens it uses. The builder makes it only after the spec is in the report.
- Tokens and fonts come from the project; never a palette of the engine's own.
- No invented data in an animated chart. `needs data:` applies here too.
- Deliver a poster frame (WebP) plus the video (WebM/MP4, muted, looped where appropriate), and a `prefers-reduced-motion` path that shows the poster. Size budget: under 2 MB on the phone viewport; otherwise cut duration or resolution.
- Keep the composition source in the repo (`assets/motion/<name>/`) with a one-line render command, so a copy change can be re-rendered.
- Critic 07 reviews the result like any other motion: timing, easing, meaning, reduced-motion path. Critic 09 checks the light direction and type against the page.

## Not for

- Anything that should be live UI motion (hover, press, entrance): that is CSS or the project's motion library, not a video.
- Photos of people, products or places. Those are real assets or missing; the brief says which.
