<div align="center">
  <h1>JHON</h1>
  <p><strong>A local co-op merge platformer built with Pygame</strong></p>
</div>

## Overview

JHON is a two-player puzzle platformer inspired by classic dual-character games. Each player controls their own character on the same keyboard; the goal is to navigate the level together and physically touch to merge. Two handcrafted levels are included plus a simple settings screen for toggling keyboard layout.

### Highlights

- Local co-op: two players on one keyboard
- Compact loop: menu → level 1 → level 2 → back to menu
- Merge-to-finish mechanic; touching advances to the next map
- Settings screen to swap QWERTY/AZERTY for Player 1
- Resizable window with automatic letterboxing; looping background music

## Controls

- Player 1 (QWERTY): move A/D, jump W
- Player 1 (AZERTY via settings): move Q/D, jump Z
- Player 2: move arrows left/right, jump arrow up
- Menu shortcuts: P = play, S = settings, Q = quit, ESC = back from settings
- Mouse: click the green buttons in settings (layout toggle, back)

## Running the game

1. Ensure Python 3.10+ is installed.
2. (Recommended) Create and activate a virtual environment:
   - Windows: `python -m venv .venv` then `.venv\Scripts\activate`
   - macOS/Linux: `python -m venv .venv` then `source .venv/bin/activate`
3. Install dependencies (only Pygame is required):
   - `pip install pygame`
   - Or run the helper file `install` if you prefer (`pip install -r` is not needed).
4. Launch: `python main.py`

## Gameplay flow

- Menu (background image `map0`): start with P or use the settings shortcut.
- Level 1 (`map1`): reach each other; merging loads Level 2.
- Level 2 (`map1` background, harder platforms): merging sends you back to the menu.
- Settings (`settings`): toggle keyboard layout button; ESC or Back returns to the menu.

## Project layout

- `main.py` bootstraps the loop, builds maps, and handles map switching.
- `entities/` contains players, walls, spikes, merge trigger, menu/settings controllers, and buttons.
- `logic/` runs the game loop, rendering, and scheduled tasks.
- `assets/` holds textures (backgrounds and entities) and audio (music + sfx).

## Notes

- The render window is resizable and maintains the map aspect ratio with letterboxing.
- Background music loops automatically; volume controls are not exposed yet.
- If assets are missing or renamed, keep the expected paths under `assets/` (see `Map` and entity textures).

## Authors

Jurian, Wannes, Tjorre, Nick, Ayman
