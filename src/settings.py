"""Configuration settings for the game."""

import json
from pathlib import Path

# Default settings
DEFAULT_SETTINGS = {
    "SCREEN_WIDTH": 400,
    "SCREEN_HEIGHT": 600,
    "WINDOW_WIDTH": 400,
    "WINDOW_HEIGHT": 600,
    "CELL_SIZE": 20,
    "FPS": 60,
    "BOARD_WIDTH": 10,
    "BOARD_HEIGHT": 20,
    "DROP_SPEED": 1000,
    "PAUSE_KEY": "p",
    "LEFT_KEY": "left",
    "RIGHT_KEY": "right",
    "DOWN_KEY": "down",
    "ROTATE_KEY": "rotate",
    # Add other defaults as needed
}

# Load user-provided settings.json if it exists
SETTINGS_PATH = Path(__file__).with_name("settings.json")
try:
    if SETTINGS_PATH.is_file():
        with SETTINGS_PATH.open("r", encoding="utf-8") as f:
            user_settings = json.load(f)
        # Ensure the loaded settings are a dict; otherwise fallback to empty
        if isinstance(user_settings, dict):
            # Merge user settings over defaults (user values win)
            merged = {**DEFAULT_SETTINGS, **user_settings}
        else:
            merged = DEFAULT_SETTINGS.copy()
    else:
        merged = DEFAULT_SETTINGS.copy()
except (json.JSONDecodeError, OSError):
    # Handle malformed or unreadable JSON gracefully
    merged = DEFAULT_SETTINGS.copy()

# Assign merged settings to the module-level SETTINGS dict
SETTINGS = merged

# Explicitly guarantee required keys exist (they should already, but safe)
SCREEN_WIDTH = SETTINGS.get("SCREEN_WIDTH", 400)
SCREEN_HEIGHT = SETTINGS.get("SCREEN_HEIGHT", 600)

# Export constants directly (they reference SETTINGS values)
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
SCREEN_WIDTH = SCREEN_WIDTH  # redundant but keeps naming consistent
SCREEN_HEIGHT = SCREEN_HEIGHT

# Define COLORS independently of SETTINGS to avoid KeyError
COLORS = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    # Add more colors as needed
}

# Define what should be exported when `from settings import *` is used
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
    "SCREEN_WIDTH",
    "SCREEN_HEIGHT",
    "COLORS",
]

# End of file