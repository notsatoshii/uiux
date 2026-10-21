# 06 Visualize

Lens: which text and numbers on the surface would land harder as a visual, and does every visual already there earn its place? Runs every cycle; leads in phase B (feel). In phase A it returns at most 3 structural findings.

## Scan: text that wants to be a visual

- numbers in prose → stat tile, comparison bars, sparkline ("3× faster" as two bars, not a sentence)
- lists of steps → numbered flow, timeline
- comparisons (before/after, us/them, plan A/B) → side-by-side, table, toggle
- categories or features → icon grid, not a bullet wall
- relationships, architecture, how it works → diagram
- a long paragraph → a visual plus one line, or a pull-quote or callout
- a table of numbers → chart, when the shape of the data matters more than the exact values

For each: the text targeted (quoted), the visual type, a one-line sketch (axes, marks, what the eye should get in two seconds), and the data source (file, API, the copy itself). A visual that needs a number the project does not have gets the fix `needs data: <what>`, never a made-up value.

## Scan: visuals already present

- Does each one say something the text next to it does not? If not, flag for removal.
- Is the chart type right for the data (parts of a whole, change over time, ranking, distribution)?
- Are the visuals one system (same palette logic, same axis style, same label font, same stroke)? Follow the project's dataviz rules if it has them.
- Does each visual read in two seconds on the phone viewport? Does it have a title that states the takeaway, not just the subject?
- Chart accessibility: a text alternative or table, labels not only by colour, hover/tap values (ties to the tooltip scan).

## Guardrail

Score on whether each visual earns its place, not on count. A landing page with thirty charts is a dashboard. The rule: every number and comparison on the page is visual, and no visual could be removed without losing meaning.

In a redesign under a "copy may not change" rule, a visual sits beside the original text; text it would replace goes to `proposed_rewrites`.

## With Appshots or Mobbin connected

Search how comparable apps show the same kind of number (`appshots_search_by_component` "Chart", "Progress", "Calendar", then `appshots_get_screens`) and propose a proven visual form; cite the screen. See `integrations/appshots.md`.

## Anchors

- **4:** the page explains its numbers and comparisons in sentences; or it has decorative charts that restate the text; or a visual shows a number that exists nowhere in the project's data.
- **7:** the key numbers and the main comparison are visual and honest; one list of steps or one comparison still lives as prose; visuals mostly share a system.
- **8:** every key number and comparison is visual, honest and titled with its takeaway; the visuals form one system and read on a phone; one secondary list or comparison could still be visual.
- **9:** every number and comparison on the page is visual, each visual states its takeaway in its title, they form one system with the brand, each reads in two seconds on a phone, and none could be removed without loss.
