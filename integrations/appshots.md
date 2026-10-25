# Appshots (reference screens)

[Appshots](https://appshots.design) is a library of real iOS, Android and web app screens and flows. It has no official connector. The community MCP server [itsOwen/appshots.design-mcp](https://github.com/itsOwen/appshots.design-mcp) uses your own Appshots login, so it can only see what your account can see. Appshots does not support it officially, so it can break when their backend changes.

## Setup (once per machine)

1. Read the server's code before you install it. At the time of writing it calls only `be.appshots.design`, Google's `securetoken` endpoint and an allowlist of image hosts.
2. Clone it and build it: `git clone https://github.com/itsOwen/appshots.design-mcp ~/tools/appshots-mcp && cd ~/tools/appshots-mcp && npm install && npm run build`.
3. Register it: `claude mcp add appshots --scope user -- node <absolute path>/dist/index.js`.
4. Log in: run `node dist/index.js auth` and paste the value of the localStorage key `firebase:authUser:<key>:[DEFAULT]` from a browser that is logged in to appshots.design. The session is saved to `~/.appshots-mcp/auth.json` and refreshes itself. Never commit or print that file.
5. Restart Claude. The tools are `appshots_search_screens`, `appshots_search_flows`, `appshots_search_by_tag`, `appshots_search_by_component`, `appshots_search_text_in_images`, `appshots_get_screens` (returns the images) and `appshots_whoami`.

## When it is present

It is the one screen library the loop is wired for. Mobbin can do the same jobs under the same rules (see `docs/sources.md`); when both are connected, record which screens came from where.

- **Orchestration 5b/5c:** run `appshots_whoami` to check the login. Build the real-app reference board from `appshots_get_screens`, on the surface's platform (`platform: ios|android|web`).
- **Interview, question 7 (references): search first, then suggest.**
  1. Search before you ask. Run `search_flows` and `search_screens` for the surface's job, `search_by_tag` for the pattern (e.g. Onboarding, Settings, Dashboard, Calendar, List) and `search_by_component` for the key component.
  2. Look at the top results as images.
  3. Suggest 3–5 apps to reference. For each one, give one line on the mechanic worth taking (e.g. "Toss: one decision per screen, the primary button fixed at the bottom") and attach 1–2 screenshots.
  4. The user confirms, removes or adds apps. Only confirmed apps go into the brief, with the mechanic and the screen URLs. Never a visual description to copy.
  5. If nothing in the library fits the category (e.g. Korean 학원 ERPs), say so and ask the user for screenshots of the competitors they know.
- **Critic 02 (references):** search the surface type and the confirmed reference apps once per cycle. Check the surface against their mechanics and cite the screen URLs in findings.
- **Critic 05 (aesthetic):** look at the top screens for the surface type to calibrate density, hierarchy and proportions. This is a bar, not a layout.
- **Critic 06 (visualize):** search for how comparable apps show the same kind of number (e.g. `search_by_component` "Chart", "Progress", "Calendar") and propose a form that has proven itself.
- **Builder:** may look at a cited screen to understand a mechanic. It may not reproduce the layout, colour story or copy rhythm.

## Rules

- The clone rule: a reference screen gives mechanics (what comes first, how proof is shown, how the first step is made easy), never the look. Any section recognisable at a glance as a library screen is a severity-2 finding.
- Screens are someone else's copyright. Keep them in the session scratchpad, never in the project repo.
- If the login has expired (a 401 or a refresh failure), say so in the summary's first line, carry on without it and tell the user how to log in again (step 4).
