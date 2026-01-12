"""Settings module for the game."""

import json
import pathlib

# Project root is the directory containing this file's parent (i.e., the repo root)
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
SETTINGS_PATH = PROJECT_ROOT / "settings.json"

# Default settings (excluding COLORS, which is defined independently)
DEFAULTS = {
    "WINDOW_WIDTH": 800,
    "WINDOW_HEIGHT": 600,
    "CELL_SIZE": 40,
    "FPS": 60,
    "BOARD_WIDTH": 10,
    "BOARD_HEIGHT": 20,
    "DROP_SPEED": 0.5,
    "PAUSE_KEY": "p",
    "LEFT_KEY": "left",
    "RIGHT_KEY": "right",
    "DOWN_KEY": "down",
    "ROTATE_KEY": "rotate",
}

# Independent hard‑coded colors dictionary
COLORS = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "YELLOW": (255, 255, 0),
    "CYAN": (0, 255, 255),
    "MAGENTA": (255, 0, 255),
    "ORANGE": (255, 165, 0),
}

# Load external settings safely
try:
    with open(SETTINGS_PATH, "r", encoding="utf-8") as f:
        user_settings = json.load(f)
    # Merge user settings into defaults; user values override defaults
    for key, value in user_settings.items():
        if key in DEFAULTS:
            DEFAULTS[key] = value
except (FileNotFoundError, json.JSONDecodeError, PermissionError):
    # If the file is missing or malformed, keep the defaults unchanged
    pass

# Export the merged settings dictionary
SETTINGS = DEFAULTS

# Export all constants via __all__
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