# Lottie (feedback moments)

Lottie files are small JSON vector animations played by `lottie-web` or `@lottiefiles/dotlottie-web`. No connector is needed; the files come from the project, from LottieFiles' free library (check each file's licence), or are exported from After Effects or made with the `lottie` tooling.

## Where they fit

Critic 07's check B, feedback moments: success check, copied-to-clipboard tick, form field valid, confetti on a completed step, an empty-state illustration that breathes, a loading mark with the brand's shape. Each is 0.3–1.5 s, plays once (loaders loop), and is recoloured to the project's tokens at load time (set the colour layers from CSS variables; do not ship a file in someone else's palette).

## Rules

- One Lottie per feedback moment, shared across the surface: all success states use the same tick.
- `prefers-reduced-motion`: show the final frame as a static SVG instead.
- Budget: under 30 KB per file, lazy-loaded; never on the critical path of the first paint.
- Accessible: the moment is also announced in text (aria-live) and not the only signal.
- Prefer the project's own icon set drawn in motion (an SVG path animation) over a third-party Lottie when the icon exists; use Lottie when the motion is richer than a stroke can carry (confetti, a character, a morph).

## Builder note

When a feedback-moment finding is fixed with a Lottie, record in the cycle report: the file, its source and licence, its size, and the token mapping used for recolouring.
