# HTML slide decks

Each sub-folder is a self-contained HTML version of the matching `.pptx` deck in `slides/`.

- `part-1/index.html` — DAPT 619 · Analytics Computing · Part 1 (71 slides, click-builds mirror the PowerPoint animations)

## Presenting

Open `index.html` in Chrome or Edge (double-click, no server needed), press `f` for fullscreen.

| Key | Action |
|---|---|
| `→` `Space` `PageDown` click | next build / slide |
| `←` `Backspace` `PageUp` shift+click | previous |
| `n` / `p` | skip builds: next / previous slide |
| `o` / `Esc` | slide overview grid |
| `f` | fullscreen |
| `b` | blackout |
| `a` | toggle animations off/on |
| `?` | help overlay |

Deep link to a slide with `index.html#12` (slide 12) or `#12.3` (slide 12, build 3).

Fonts (Space Grotesk, Inter, JetBrains Mono) load from Google Fonts; offline, the deck falls back to system fonts and everything else still works.

## Embedded video (slide 69)

YouTube refuses to play inside a page opened as a local file, so when you double-click `index.html` that slide shows a thumbnail that opens YouTube in a new tab. To play it inline, run `present.cmd` (Windows) or `./present.sh` (WSL/macOS/Linux) in the deck folder: it serves the deck at http://localhost:8619 and opens the browser.
