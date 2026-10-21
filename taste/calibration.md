# Calibration board

Words drift; pictures do not. The calibration board is a folder of real screens the owner approved and rejected, with their words. The taste critics (05, 08, 09), the fresh-eyes check, the direction judge and the builder look at it next to the surface. It is how "9" and "4" mean what the owner means.

## Where

Next to the owner's taste file: `$UIUX_TASTE_DIR/calibration/` if set, else `~/.claude/uiux/calibration/`. Private, synced with the taste file. Never in a project repo (screens of other products are someone else's copyright; the owner's own are fine anywhere, but keep one place).

```
calibration/
  index.md
  approved/<date>-<project>-<screen>.png
  rejected/<date>-<project>-<screen>.png
```

`index.md`, one line per image:

```
- approved · 2026-10-04 · innovlabs · home hero (R4b) · approved/2026-10-04-innovlabs-home.png · "combine r3 and the 3d test board clay" · big few clay objects behind frosted glass
- rejected · 2026-10-20 · oratio · home (v1) · rejected/2026-10-20-oratio-home-v1.png · "tacky" · brand colours as fills, gold shapes standing in for photos, heavy wide display type
```

Fields: verdict, date, project, screen, file, the owner's words (quoted), what the picture teaches in one line.

## How it fills

- **Direction step:** the chosen direction goes to approved, every rejected direction to rejected, with the owner's words.
- **Owner previews:** a negative reaction ("tacky", "cheap", "bad") adds that screen to rejected; a clear positive ("that's it", "love this") adds it to approved.
- **Shipped work:** at the end of a run, if the owner approved the final in a preview, its key screen goes to approved.
- **`/uiux taste init`:** the pairs interview's picks are saved as small approved/rejected pairs.
- **By hand:** `/uiux taste add-shot <file> approved|rejected "<words>"`.

Keep it small: at most about 12 approved and 12 rejected. When a new image teaches the same lesson as an old one, replace the old.

## How it is read

- **Critic 05 (aesthetic):** before scoring, look at the approved and rejected images. The 9 anchor is "would sit next to the approved images"; the 4 anchor is "shares the failure named on a rejected image". Name the closest image and why. A surface that repeats a rejected image's named failure cannot score above 5, whatever else it does.
- **Critics 08 and 09, the builder:** read the lessons in `index.md` before making anything new.
- **Fresh-eyes check and direction judge:** see the approved images as "the owner's level" alongside the reference board, without the words.
- An empty or missing board is noted in the brief; on the first run the orchestrator offers `/uiux taste init` once and seeds the board from the owner's earlier projects when the host knows them.
