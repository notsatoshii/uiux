# Mobbin (reference screens)

Mobbin is a library of real app and web screens and flows. In Claude it is a connector named **Mobbin** (`search_flows`, `search_screens`, `search_sections`); it needs a paid Mobbin account and is connected by the user in Connectors → Browse. In the Claude Code CLI the community server `mobbin-mcp` (`npx -y mobbin-mcp auth`, then `claude mcp add mobbin -- npx -y mobbin-mcp`) does the same.

## When it is present

- **Interview, question 7 (references):** for each reference the user names, and for the surface type, search flows and sections once and show the user two or three candidate *mechanics* with the screen they come from. The user picks. The brief records the mechanic and the Mobbin screen id, never a visual description to copy.
- **Critic 02 (references):** search the surface's type (e.g. "pricing page", "onboarding fork", "academy landing") and the brief's references; pull the mechanics (order of sections, how proof is shown, how the ask is framed, first-step friction) from the top results and check the surface against them. Cite the screens in findings.
- **Critic 05 (aesthetic):** search the surface type once and look at the top screens to calibrate what good density, hierarchy and section order look like for this kind of page. This is the taste use (`taste/README.md`, item 7): a bar, not a layout.
- **Critic 06 (visualize):** search for how comparable products show the same kind of number or comparison, to propose a proven visual form.
- **Builder:** may look at a cited screen to understand a mechanic. May not reproduce its layout, colour story or copy rhythm. The references critic checks for clones next cycle.

## The clone rule, restated

A reference screen gives mechanics: what comes first, what is shown as proof, how the first step is made easy, how a toggle or a comparison is structured. It never gives the look. If a section of the surface would be recognised as a Mobbin screen at a glance, that is a severity-2 finding.

## When it is absent

The references critic works from its own knowledge of the named products and says so in the first line of its summary. Nothing else changes.
