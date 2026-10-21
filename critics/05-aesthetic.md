# 05 Aesthetic

Lens: does the surface look like this brand, with intent, and not like the statistical average of the web? Judge against the brief's three words, three anti-words and visual world, never against your own taste.

## Checks

- **The logo test:** cover the logo. Is the page still recognisably this brand, or could it be any competitor's? (The reference's "Zombie UI" test.)
- **Slop:** go through `taste/slop.md` item by item. Each one present without a reason in the brief is a finding; three or more on one screen cap this score at 5.
- **The taste bar:** name the reference in `taste/references.md` or the project's `taste.md` that the surface comes closest to, and the gap. "Closest to nothing in particular" is itself a finding: the surface has no point of view.
- **Hierarchy:** where does the eye land first, second, third? Does that order match the one job? Run `tools/sightline.py` on the hero screenshot (phone viewport) and quote its three regions; then squint yourself and say whether you agree. The script's rank 1 should be the one job's element or the headline that leads to it; anything else is a finding with the map as evidence.
- **The three words:** for each adjective in the brief, point at the element that delivers it. For each anti-word, point at anything that leaks it. An adjective with no element delivering it is a finding.
- **Composition:** rhythm of sections (not all the same height and density), whitespace with intent, alignment to a grid, image and illustration treatment consistent, colour used to mean something.
- **Typography:** the type does real work (contrast of size and weight, measure 45–75 characters, tight headings, comfortable body), and the pairing fits the visual world.
- **Pacing:** the loud and quiet zones from the brief are where the brief put them.
- **Mode fit:** persuade surfaces earn attention; operate surfaces stay out of the way; read surfaces make reading pleasant; experience surfaces let the work lead.

- **Side by side:** open the real-app reference board (orchestration 0.5c) next to this cycle's phone shots. Compare proportions, not components: how much of the screen is accent colour, how heavy the headings are, how much decoration there is, how much empty space. Name the single biggest difference.

## Score cap

The score cannot go above 6 while the surface looks cheaper, louder or more decorated than the reference board, whatever the brief's adjectives say ("regal", "bold", "confident" are not licences for decoration). Quote the difference you named.

## With Appshots or Mobbin connected

Look at the top screens for the surface type once (`appshots_search_by_tag` / `appshots_get_screens`, or Mobbin) to calibrate density, hierarchy and proportions. A bar, not a layout. See `integrations/appshots.md`.

## Anchors

- **4:** fails the logo test; two or more slop items; the hero is the generic layout; the three words are not visible in any element; sections all look alike; closest reference: none.
- **7:** on-brand and clearly intended; no slop; the three words are each delivered somewhere; one section still breaks the world (a stock-looking card row, a type size out of scale, a section that leaks an anti-word); you can name the reference it is reaching for and the gap is one or two things.
- **9:** distinct at a glance without the logo; every section reads as the same brand with its own rhythm; the eye path matches the one job; nothing on the page could be swapped for a template; it stands next to its closest reference without embarrassment; a designer would ask who made it.
