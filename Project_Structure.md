# Project Structure

## Directory Layout

```
project_root/
├─ src/
│   ├─ main.py
│   ├─ game.py
│   ├─ tetromino.py
│   ├─ board.py
│   ├─ piece.py
│   ├─ utils.py
│   └─ settings.py
├─ assets/
│   ├─ images/
│   │   ├─ background.png           # 800x600
│   │   ├─ board_tile.png           # 30x30
│   │   ├─ tetromino_I.png          # 30x30
│   │   ├─ tetromino_J.png          # 30x30
│   │   ├─ tetromino_L.png          # 30x30
│   │   ├─ tetromino_O.png          # 30x30
│   │   ├─ tetromino_S.png          # 30x30
│   │   ├─ tetromino_T.png          # 30x30
│   │   ├─ tetromino_Z.png          # 30x30
│   │   └─ tetromino_SpriteSheet.png  # optional 210x30 (7 pieces * 30)
│   └─ sounds/
│       ├─ line_clear.wav
│       ├─ rotate.wav
│       ├─ drop.wav
│       └─ game_over.wav
├─ data/
├─ tests/
├─ README.md
├─ requirements.txt
└─ .gitignore
```

## Core Source Files

- **src/main.py** – Entry point, initializes Pygame and starts the game loop.  
- **src/game.py** – Manages game state, input handling, and overall flow.  
- **src/tetromino.py** – Defines Tetromino class and its shapes/rotations.  
- **src/board.py** – Represents the playing board, collision detection, and line clearing.  
- **src/piece.py** – Encapsulates a single falling piece (position, shape, rotation).  
- **src/utils.py** – Helper functions (e.g., matrix operations, color utilities).  
- **src/settings.py** – Game configuration constants (colors, speeds, grid size).  
- **src/config.json** – External JSON configuration for adjustable settings.  

## Asset Details

- **images/background.png** – 800 × 600 PNG, used as the game background.  
- **images/board_tile.png** – 30 × 30 PNG, individual tile graphic for the board.  
- **images/tetromino_*.png** – 30 × 30 PNG files for each of the 7 tetromino shapes (I, J, L, O, S, T, Z).  
  - Alternatively, a single **images/tetromino_SpriteSheet.png** (210 × 30 PNG) may be used to contain all shapes side‑by‑side.  
- **sounds/line_clear.wav** – Sound effect played when a line is cleared.  
- **sounds/rotate.wav** – Sound effect for piece rotation.  
- **sounds/drop.wav** – Sound effect when a piece drops.  
- **sounds/game_over.wav** – Sound effect for game‑over event.  

All sound files are standard WAV format, typically short (<1 s) effects.

---  

*The above structure provides a clear organization for source code, assets, data, and tests, making the project easy to navigate and extend.*\n