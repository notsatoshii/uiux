# Sources and references

What uiux borrows, and from where. Ideas are borrowed; no vendor is required.

## Tools and connectors the loop can use

| Thing | What it is | Link |
|---|---|---|
| Claude Code skills | How a folder with a SKILL.md becomes a slash command | https://code.claude.com/docs/en/skills |
| Claude Code subagents | How the critics run in parallel | https://code.claude.com/docs/en/sub-agents |
| MCP connectors | How Mobbin and HyperFrames attach to Claude | https://code.claude.com/docs/en/mcp |
| Mobbin | Library of real app and web screens and flows; connector "Mobbin" | https://mobbin.com |
| HyperFrames (HeyGen) | HTML + GSAP video compositions for coding agents; connector and skills | https://github.com/heygen-com/hyperframes |
| Remotion | React video framework with official agent skills | https://www.remotion.dev/docs/ai/claude-code |
| Lottie | JSON vector animation format and players | https://lottiefiles.com · https://github.com/airbnb/lottie-web · https://github.com/LottieFiles/dotlottie-web |
| Pillow | Python imaging library used by `tools/` | https://python-pillow.org |
| FFmpeg | Frame extraction for `tools/frames.py` | https://ffmpeg.org |
| Playwright | Fallback screenshots | https://playwright.dev |
| impeccable | Design skill with the shape/critique/audit/polish playbooks and the persuade/operate/read/experience modes uiux reuses | https://github.com/pbakaus/impeccable |
| ASD-STE100 | Simplified Technical English, the writing standard for this README | https://www.asd-ste100.org |

## Design and craft ideas

| Idea in uiux | Where it comes from | Link |
|---|---|---|
| Brand point of view before pixels; the "logo test"; Zombie UI | A 2026 talk-turned-guide on AI design systems (shared with the author as a note; it names Stripe's design practice as the example) | https://stripe.com/blog/engineering (Stripe's engineering and design writing) |
| "Done is not good": post-build editing, the numbered micro-craft list ("Pepsi-bubbling") | Same source; the practice of a 17-point critique list on one small graphic | — |
| Take mechanics, never visuals; no 1:1 clones | Same source; the "Castle clone" case | — |
| Scroll journey, core belief, real-asset audit, signature move, emotional pacing, receipts | Nate Herk's Scrollcraft interview (five discovery questions) and its "receipt-driven proof" | — (no public page known; described in the same note) |
| Video to motion spec | The "video-to-super-prompt" idea: read timing from frames instead of describing it in words | — |
| Pixel token extraction | The "Tastemaker" idea: measure a reference instead of summarising it | — |
| Sightline / attention map | Research-grounded screen critique: where the eye lands first | https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/ |
| Perception and cognitive-load heuristics | Laws of UX | https://lawsofux.com |
| Gutenberg's 290 characters: encode the standard into the machine | Same source; general history | https://en.wikipedia.org/wiki/Johannes_Gutenberg |

## Behavioural research behind the references critic

| Pattern | Study | Link |
|---|---|---|
| Smart defaults, fewer choices | Iyengar & Lepper 2000, the jam study | https://doi.org/10.1037/0022-3514.79.6.995 |
| Goal gradient, never start at 0 % | Nunes & Drèze 2006, the endowed progress effect | https://doi.org/10.1086/500480 |
| Reciprocity, value before the gate | Cialdini, Influence (principles of persuasion) | https://www.influenceatwork.com/7-principles-of-persuasion/ |
| IKEA / endowment effect | Norton, Mochon & Ariely 2012 | https://doi.org/10.1016/j.jcps.2011.08.002 |
| Loss aversion | Kahneman & Tversky 1979, prospect theory | https://doi.org/10.2307/1914185 |
| Anchoring | Tversky & Kahneman 1974 | https://doi.org/10.1126/science.185.4157.1124 |

## Standards the best-practices critic uses

| Standard | Link |
|---|---|
| WCAG 2.2 | https://www.w3.org/TR/WCAG22/ |
| prefers-reduced-motion | https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion |
| hover media query (touch-safe hover) | https://developer.mozilla.org/en-US/docs/Web/CSS/@media/hover |
| Core Web Vitals | https://web.dev/articles/vitals |

## Named practitioners in the source note

The note that started this project names these people and their skills. uiux does not include their work; it names them so you can look them up: Emil Kowalski (design engineering, animation vocabulary), Mangto (awards-quality sites, video-to-prompt), Connard Lee (web design engineer), Eliia Design (single-action landing pages), Jakob Creel (review and layout skills), Tastemaker, Nate Herk (Scrollcraft), Brendan Jowett (the clone benchmark).
