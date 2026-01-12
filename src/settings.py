import json
from pathlib import Path

# Resolve settings.json relative to the project root (one level up from src/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SETTINGS_PATH = PROJECT_ROOT / "settings.json"

# ----------------------------------------------------------------------
# Default settings – used if the file is missing or malformed
# ----------------------------------------------------------------------
_DEFAULTS = {
    "WINDOW_WIDTH": 800,
    "WINDOW_HEIGHT": 600,
    "CELL_SIZE": 30,
    "FPS": 60,
    "BOARD_WIDTH": 10,
    "BOARD_HEIGHT": 20,
    "DROP_SPEED": 1000,  # milliseconds
    "PAUSE_KEY": "p",
    "LEFT_KEY": "left",
    "RIGHT_KEY": "right",
    "DOWN_KEY": "down",
    "ROTATE_KEY": "rotate",
}

# Load settings.json safely
try:
    if SETTINGS_PATH.is_file():
        with SETTINGS_PATH.open("r", encoding="utf-8") as f:
            _user_settings = json.load(f)
        # Ensure we have a dict; if not, fall back to defaults
        if not isinstance(_user_settings, dict):
            raise ValueError("settings.json must contain a JSON object")
        # Merge user settings over defaults (user values take precedence)
        SETTINGS = {**_defaults, **_user_settings}
    else:
        SETTINGS = _DEFAULTS.copy()
except (json.JSONDecodeError, ValueError, OSError) as exc:
    # Any error (missing file, bad JSON, permission issue) falls back to defaults
    SETTINGS = _DEFAULTS.copy()


# ----------------------------------------------------------------------
# Export constants using values from SETTINGS or fall back to defaults
# ----------------------------------------------------------------------
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

# ----------------------------------------------------------------------
# Independent hard‑coded colors dictionary – DO NOT load from SETTINGS
# ----------------------------------------------------------------------
COLORS = {
    "background": (0, 0, 0),
    "grid": (40, 40, 40),
    "text": (255, 255, 255),
    "block": (0, 255, 0),
    "next": (255, 165, 0),
}

# ----------------------------------------------------------------------
# Define what should be exported when `from settings import *` is used
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