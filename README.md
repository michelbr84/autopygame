# Tetris-Style Game
A simple Tetris-like game implemented in Python using Pygame.

## Requirements
- Python 3.13+
- Pygame (install with `pip install -r requirements.txt`)

## Installation
1. Place all images (PNG) in `assets/images/`.
2. Place all sounds (WAV) in `assets/sounds/`.
3. Ensure the folder structure matches the `Assets.md` file.

## Running the Game
The project is structured as a Python package under `src/`. To run the game, execute:
```bash
python -m src.main
```
Alternatively, you can add `src` to your `PYTHONPATH` and run:
```bash
python src/main.py
```

## Settings
Edit `settings.json` in the project root to customize window size, cell size, FPS, drop speed, etc.

## Controls
- ← / → : Move piece left/right
- ↓ : Soft drop
- ↑ : Rotate piece
- Space : Hard drop
- Esc : Quit

## License
This project is licensed under the MIT License.