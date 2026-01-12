import json
from pathlib import Path

# Resolve settings.json located at the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SETTINGS_PATH = PROJECT_ROOT / "settings.json"

# Load JSON
with SETTINGS_PATH.open('r') as f:
    SETTINGS = json.load(f)

# Export individual constants from the loaded settings
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
COLORS = SETTINGS["COLORS"]

# Re-export the SETTINGS dict for convenience
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