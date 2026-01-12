"""
settings.py - Central configuration loader for the Tetris‑style game.

- Loads Settings.json from the project root into a module‑level `SETTINGS` dict.
- Provides fallback default values if the JSON file is missing or malformed.
- Exports all required constants (WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE,
  FPS, BOARD_WIDTH, BOARD_HEIGHT, DROP_SPEED, PAUSE_KEY, LEFT_KEY,
  RIGHT_KEY, DOWN_KEY, ROTATE_KEY) using the merged `SETTINGS` values or
  defaults.
- Defines `COLORS` as its own hard‑coded dictionary (do **not** fetch it
  from `SETTINGS`) to avoid KeyError.
- Declares `__all__` to explicitly export `SETTINGS` and all constants.
- Safely handles missing or malformed configuration files.
"""

import json
import pathlib
import sys

# ----------------------------------------------------------------------
# Resolve the path to settings.json relative to this file (project root)
# ----------------------------------------------------------------------
PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
SETTINGS_PATH = PROJECT_ROOT / "settings.json"

# ----------------------------------------------------------------------
# Default configuration values
# ----------------------------------------------------------------------
DEFAULTS = {
    "WINDOW_WIDTH": 400,
    "WINDOW_HEIGHT": 600,
    "CELL_SIZE": 30,
    "FPS": 60,
    "BOARD_WIDTH": 10,
    "BOARD_HEIGHT": 20,
    "DROP_SPEED": 1000,
    "PAUSE_KEY": "p",
    "LEFT_KEY": "left",
    "RIGHT_KEY": "right",
    "DOWN_KEY": "down",
    "ROTATE_KEY": "up",
    # Note: COLORS is defined separately (see below) and should NOT be loaded
    # from the JSON file.
}

# ----------------------------------------------------------------------
# Load SETTINGS from JSON if it exists; otherwise use defaults
# ----------------------------------------------------------------------
try:
    if SETTINGS_PATH.is_file():
        with SETTINGS_PATH.open("r", encoding="utf-8") as f:
            user_cfg = json.load(f)
        # Merge user config over defaults (keep defaults for missing keys)
        SETTINGS = {**DEFAULTS, **user_cfg}
    else:
        SETTINGS = DEFAULTS.copy()
except (json.JSONDecodeError, OSError) as e:
    # On any error, fall back to defaults and optionally log/print
    SETTINGS = DEFAULTS.copy()
    # Optionally, you could print a warning here:
    # print(f"Warning: Could not load '{SETTINGS_PATH}': {e}")

# ----------------------------------------------------------------------
# Hard‑coded colors dictionary (do NOT load from SETTINGS)
# ----------------------------------------------------------------------
COLORS = {
    'I': (0, 255, 255),
    'O': (255, 255, 0),
    'T': (128, 0, 128),
    'S': (0, 255, 0),
    'Z': (255, 0, 0),
    'J': (0, 0, 255),
    'L': (255, 165, 0),
}

# ----------------------------------------------------------------------
# Export public symbols
# ----------------------------------------------------------------------
__all__ = [
    "SETTINGS",
    "WINDOW_WIDTH",
    "WINDOW_HEIGHT",
    "CELL_SIZE",
    "FPS",
    "BOARD_WIDTH",
    "BOARD_HEIGHT",
    "DROP_SPEED",
    "PAUSE_KEY",
    "LEFT_KEY",
    "RIGHT_KEY",
    "DOWN_KEY",
    "ROTATE_KEY",
    "COLORS",
]

# Optionally expose individual constants for convenience
# (they are also available via SETTINGS, but this makes them direct attributes)
WINDOW_WIDTH = SETTINGS["WINDOW_WIDTH"]
WINDOW_HEIGHT = SETTINGS["WINDOW_HEIGHT"]
CELL_SIZE = SETTINGS["CELL_SIZE"]
FPS = SETTINGS["FPS"]
BOARD_WIDTH = SETTINGS["BOARD_WIDTH"]
BOARD_HEIGHT = SETTINGS["BOARD_HEIGHT"]
DROP_SPEED = SETTINGS["DROP_SPEED"]
PAUSE_KEY = SETTINGS["PAUSE_KEY"]
LEFT_KEY = SETTINGS["LEFT_KEY"]
RIGHT_KEY = SETTINGS["RIGHT_KEY"]
DOWN_KEY = SETTINGS["DOWN_KEY"]
ROTATE_KEY = SETTINGS["ROTATE_KEY"]