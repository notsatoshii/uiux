# Open Design (workspace, skills, HyperFrames rendering)

[Open Design](https://github.com/nexu-io/open-design) is a local-first design workspace (Next.js + a Node daemon + an Electron app, Apache-2.0) that uses your own coding agent as the engine. It makes prototypes (single-page HTML for web, desktop and mobile), live dashboards, decks (HTML, PDF, PPTX), images (BYOK) and motion/video (HyperFrames: agent-written HTML, CSS and GSAP rendered to MP4 with headless Chrome and FFmpeg). It ships 100+ skills, design systems and templates, an `od` CLI with `--json` on most commands, and a stdio MCP server.

## Install

```bash
git clone https://github.com/nexu-io/open-design.git <tools>/open-design
cd <tools>/open-design && pnpm install        # Node ~24, pnpm 10.33.x (corepack, or npm i -g pnpm@10.33.2)
pnpm tools-dev run web                        # the workspace at http://127.0.0.1:7456
od mcp install claude                         # registers the MCP server in Claude Code
```

Or the desktop app from open-design.ai. The daemon binds to 127.0.0.1 and is read-only by default. On macOS and WSL2 the system `od` (octal dump) can shadow the CLI; use the full path.

## How uiux uses it

- **Orchestrator, intake:** if the `od` MCP server is present, record it in the brief's House rules. Projects can be mirrored into an Open Design project so the owner reviews cycles in its UI (`od project list --json`, `od files read <project> <path>`).
- **Builder, generated motion assets:** `integrations/motion-assets.md` names HyperFrames as the engine for HTML sites. Open Design is one way to run it: its motion skills compose the HTML and its renderer produces the MP4 and a poster. The spec goes in the cycle report first; tokens come from the project.
- **Builder, decks and dashboards:** out of uiux's scope (uiux loops on a surface in a codebase). If a brief's asset gap is a deck or a one-off dashboard, hand it to Open Design and link the result.
- **Critic 02 (references):** Open Design's design-system packs (`design-systems/`) are mechanics references for section order and density, under the same no-clone rule as Mobbin.
- **Critic 07 (motion):** Open Design's `review-animations` skill, when installed, is run as a second opinion on the motion check; its findings are merged under critic 07 with the source named.

## Rules

- Open Design generates into its own project folder. Anything that ends up in the codebase goes through the builder and the project's tokens; never copy a generated page in whole.
- Image generation is BYOK; a generated image is "may be generated" material only where the brief allows it, and never a photo of a real person, product or place.
- The MCP server is read-only by default; keep it so unless the owner turns writes on for a reason.

## When it is absent

Nothing in the loop depends on it. HyperFrames can run from its own skills (`npx skills add heygen-com/hyperframes`); motion recipes come from `integrations/motion-anything.md`.
