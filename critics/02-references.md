# 02 References

Lens: does the surface use the proven mechanics of the brief's references, without copying their look?

## Method

1. For each reference in the brief, write down (from your own knowledge of that product; do not browse unless a tool is offered) the two or three mechanics worth having here: order of sections, how proof is shown, how the price or the ask is framed, how the first action is made easy, how empty states invite. Mechanics only.
2. Check the surface against each mechanic: present, partial, absent, or not applicable to this mode.
3. Check for cloning: a section that would be recognised as the reference's at a glance (same layout, same colour story, same copy rhythm) is a severity-2 finding. Mechanics are free; looks are not.
4. Check the conversion patterns that apply to the mode, from behavioural research, as mechanics:
   - smart defaults instead of empty fields
   - goal gradient: never show 0% progress
   - reciprocity: value before the gate
   - endowment: let the visitor shape something before asking them to sign up
   - loss framing where a real loss exists (never invented)
   - anchoring where there is a real anchor (never invented)
   Flag a pattern as a finding only when it fits the one job; a docs page does not need a pricing anchor.

## Receipt scan

Every claim and every number on the surface, listed, with: its evidence (from the brief's receipts), and whether the page shows the evidence (footnote, source link, drawer, live figure, screenshot). A claim with no evidence is severity 1 (`needs data:` or cut). Evidence that exists but is not shown is severity 2. A live number (API or data file) beats a typed one; a typed number needs a date next to it.

## With Appshots connected

Search the surface's type and the brief's confirmed reference apps once (`appshots_search_flows`, `appshots_search_screens`, `appshots_search_by_tag`, then `appshots_get_screens` to look); take the mechanics from the top results and cite the screen ids in findings. See `integrations/appshots.md`. Without it, say so in the summary's first line.

## Anchors

- **4:** the references are ignored or copied. The page's order of sections is the generic default (hero, three features, testimonials, CTA) regardless of the one job; proof is a claim with no evidence; the first action asks for commitment before giving anything.
- **7:** the main mechanics are there (the ask is framed well, proof exists, the first step is easy); one reference's lesson is missing or one section leans too close to a reference's look.
- **8:** every main mechanic of the confirmed references is present and works in the walk log; proof is shown, not claimed; no section reads as a copy; one secondary mechanic is still missing or weaker than the reference's.
- **9:** every applicable mechanic is present and reads as this brand's; a visitor who knows the references would not name them; the conversion patterns that fit the one job are all in place and none is faked.
