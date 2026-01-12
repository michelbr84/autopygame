# Project Structure

This document outlines the complete directory and file structure for the Python Pygame project.

```
project-root/
├── assets/
│   ├── images/
│   │   ├── background.png
│   │   ├── player.png
│   │   ├── enemy.png
│   │   ├── bullet.png
│   │   └── ...
│   └── sounds/
│       ├── hit.wav
│   │   └── pickup.wav
│   └── fonts/
│       └── pixel_font.ttf
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── player.py
│   ├── enemy.py
│   ├── bullet.py
│   ├── utils.py
│   └── settings.py
├── config/
│   └── settings.yaml   # game configuration (optional)
├── requirements.txt
├── README.md
└── Project_Structure.md
```

## Details

- **assets/images**: Holds all PNG images used in the game. Each image file is referenced by its logical name (e.g., `player.png`).
- **assets/sounds**: Holds all audio files (WAV/OGG) used for sound effects and background music.
- **assets/fonts**: Holds custom font files (TTF/OTF) for rendered text.
- **src**: Contains all Python source code.
  - **main.py**: Entry point; initializes Pygame, loads assets, and runs the game loop.
  - **player.py**: Player character class and related logic.
  - **enemy.py**: Enemy character class and related logic.
  - **bullet.py**: Bullet/sprite class.
  - **utils.py**: Helper functions and constants.
  - **settings.py**: Global constants (screen size, FPS, colors, etc.).
- **config**: Optional external configuration files (e.g., YAML for difficulty settings).
- **requirements.txt**: Python dependencies (e.g., `pygame`).
- **README.md**: High‑level project description and usage instructions.
- **Project_Structure.md**: This file.

## Asset Requirements

- All image assets must be in **PNG** format unless otherwise noted, with dimensions specified in the asset list (see `Assets.md`).
- Sound assets must be in **WAV** or **OGG** format.
- Font files should be **TTF** or **OTF**.

Once all assets are placed in the appropriate subfolders under `assets/`, the game can be run by executing `python src/main.py`.

*Commit this structure to the repository to ensure reproducibility and ease of onboarding for new developers.*
