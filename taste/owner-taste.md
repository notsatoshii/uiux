# The owner's taste file

One file per person, across every project and machine. It is a log of real decisions, not a list of adjectives: what they chose, what they rejected, in their words, with the date and the project. The critics and the builder read it second, after the project's `taste.md` and before the skill's own taste.

Location: `$UIUX_TASTE` if set, else `~/.claude/uiux/taste.md`. Keep it outside project repos. Symlink it into a private synced folder if you work on more than one machine.

## Format

```markdown
# <name>'s taste

## Likes
- <date> · <project> · "<their words>" → <what it means for a build, one line>

## Dislikes
- <date> · <project> · "<their words>" → <what to avoid, one line>

## Picks (A/B decisions)
- <date> · <project> · chose <A> over <B> because "<their words>"

## Closest references
- <reference> for <what> (their words if they named it)

## Standing rules (confirmed twice or more)
- <rule> (first <date>, again <date>)
```

A line moves to Standing rules once the owner has said the same thing on two occasions. Standing rules are the part the critics quote in findings.

## How it is seeded: `/uiux taste init`

1. Import: read what the host already knows about the owner's design preferences (memory files, earlier briefs, `taste.md` files in their projects) and list it back, each line as a quote with its date; the owner confirms or strikes each.
2. Pairs interview, ten rounds at most. Each round shows two directions for the same thing and asks which, and why in a few words. Rounds: ground (warm tint vs cool tint), ink (black vs tinted dark), display type (grotesk vs serif vs one with character), density (airy vs dense), shadows (none vs tinted soft), radius (sharp vs rounded), colour (one accent vs several), motion (none vs explanatory vs playful), imagery (photo vs illustration vs 3D), hero (product-first vs statement-first). Render each pair as a small comparison (an artifact or two screenshots), never as prose, so the pick is visual.
3. Write the file. Read it back in five lines. Stop.

## How it grows: capture

During a run, every time the owner reacts to a preview, a screenshot or a cycle report with a judgement about the look (not about facts or copy), the orchestrator appends the reaction to the file under Likes or Dislikes, quoted and dated, with the project name. Examples of what counts: "the previous one was better", "too much", "that is it", "I hate the small stickers", "more like the test board". What does not count: facts, copy edits, bug reports, priorities.

The orchestrator writes these at the end of the run (step 4, Report), not mid-cycle, and lists what it added in the chat summary so the owner can strike a line.

`/uiux taste add "<note>"` appends a line by hand. `/uiux taste show` prints the file. `/uiux taste promote` moves repeated lines to Standing rules and shows the result.

## How it is read

- Critic 05 (aesthetic) quotes the owner's Standing rules and Dislikes in findings where they apply, and names the owner's Closest references when it scores the taste bar.
- Critics 06–09 and the builder read Likes, Dislikes and Standing rules before making or judging anything new.
- Nothing in the file overrides the brief's three words or the house rules for the surface. Where they conflict, the brief wins for that surface and the critic says so in one line.
