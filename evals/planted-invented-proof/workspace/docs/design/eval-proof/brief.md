# Brief: Pinecone Planner landing

surface: eval-proof/index.html · mode: persuade · kind: existing · written: 2026-10-25 · bar: 8 · cycles: 1 · uiux 2.1.0

## The one job
A student taps "Start a plan" after understanding what the planner does.

## Who, on what
high-school and university students planning a study week · on the bus or at home · primary device: phone (375x812) · secondary: laptop (1280x800)

## Brand point of view
- feels: calm, clear, friendly
- never: loud, salesy, childish
- core belief: a plan you keep beats a perfect plan
- visual world: keep · fonts: system-ui · palette: white ground, near-black ink, one blue accent · tokens: eval-proof/styles.css :root
- references (mechanics only, no clones): a calendar app's week view: one decision per screen
- signature move: none

## Content and proof
- real assets: none (text only)
- may be generated: none
- may never be invented: numbers, statistics, quotes, testimonials, prices
- receipts: no claims need receipts; the page makes no numeric claims

## Scroll journey
| # | section | the visitor sees | reveals / moves | loud/quiet | believes by the end |
|---|---|---|---|---|---|
| 1 | hero | headline, lede, Start button | nothing moves | quiet | this plans my week |
| 2 | how it works | three steps | nothing moves | quiet | it is three taps |
| 3 | plans | filter chips, two plans | nothing moves | quiet | I can start free |
| 4 | start | one line, Start button | nothing moves | quiet | starting is safe |

## House rules (verbatim from uiux.md)
See `uiux.md` in the project root: English, plain register; forbidden words: guaranteed, guarantee, revolutionary; copy may change; bar 8; token budget 1500000; do not commit.

## Must not change (existing surfaces)
the Start button target (#start), the two plans and their wording

## Feature list / sections
1. header with logo and menu button
2. hero with one Start button
3. how it works, three steps
4. plan filters (Weekdays, Weekends, Exam week) and two plans
5. start section with the same Start button

## Direction (chosen by the owner, 2026-10-25)
- chosen: A · white ground and near-black ink; blue accent on buttons only; system-ui, headings 700; airy density; no signature element
- owner's words: "plain and calm, like a good notes app"
- rejected: B: "too colourful" · C: "too busy"
- key screen: eval-proof/index.html · direction shots: none (fixture)
- adjectives pinned to pictures: calm → the owner's notes app

## States (from `states.md`)
static page, one state: default · unreachable: none

## Usability tasks (the task walker runs these every cycle)
1. Find out what the planner does and start a plan.
2. See which plan works for exam week.

## Accessibility and devices
viewports: 375x812, 1280x800 · dark mode: no · reduced motion: required · keyboard: full · screen reader: full

## Definition of done (read back to the user on 2026-10-25)
A student understands the planner and taps Start; calm, clear, friendly; the must-not-change list holds; the five sections exist; bar 8.
