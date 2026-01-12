import json
from pathlib import Path

# Resolve settings.json relative to project root
try:
    PROJECT_ROOT = Path(__file__).resolve().parents[1]  # src/ is one level down from project root
    SETTINGS_PATH = PROJECT_ROOT / "settings.json"
    with SETTINGS_PATH.open("r", encoding="utf-8") as f:
        _raw = f.read()
        SETTINGS = json.loads(_raw) if _raw.strip() else {}
except (FileNotFoundError, json.JSONDecodeError):
    # Fallback defaults if file missing or malformed
    SETTINGS = {}

# Fallback defaults for required keys
DEFAULTS = {
    "WINDOW_WIDTH": 800,
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
    "ROTATE_KEY": "rotate",
}
# Merge defaults with loaded settings
SETTINGS = {**DEFAULTS, **SETTINGS}

# Export constants (uppercase names)
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

# Hard‑coded COLORS dictionary (independent of SETTINGS)
COLORS = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "YELLOW": (255, 255, 0),
    "CYAN": (0, 255, 255),
    "MAGENTA": (255, 0, 255),
    "GRAY": (128, 128, 128),
}

# Public API declaration
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