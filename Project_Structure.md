# Tetris Game Project Structure

## Directories

- `src/`: Contains all source code.
  - `main.py`: Entry point of the game.
  - `tetris.py`: Core game logic.
  - `pieces.py`: Tetromino definitions.
  - `ui.py`: UI rendering functions.
- `assets/`: Contains all game assets.
  - `images/`: Image assets.
    - `background.png`: Background image.
    - `block.png`: Generic block image (used for all shapes).
    - `block_i.png`, `block_j.png`, `block_l.png`, `block_o.png`, `block_s.png`, `block_t.png`, `block_z.png`: Colored block variations.
  - `sounds/`: Sound assets.
    - `clear_line.wav`: Sound effect for clearing a line.
    - `drop.wav`: Sound effect for piece drop.
    - `game_over.wav`: Game over jingle.
- `docs/`: Documentation files.
  - `Project_Structure.md`: This file.
  - `README.md`: Project README (already present).
- `requirements.txt`: Python dependencies (e.g., pygame).

## Files

- `config.py`: Game configuration constants (colors, speeds, grid size).
- `assets.md`: Asset manifest with file paths and descriptions.
- `.gitignore`: Git ignore file.