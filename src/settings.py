import json
import pathlib
import sys

# Resolve settings.json relative to project root (the directory containing src/)
PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]  # src/ is inside, project root is one level up
SETTINGS_PATH = PROJECT_ROOT / "settings.json"

# Load settings.json with error handling
try:
    with open(SETTINGS_PATH, "r") as f:
        SETTINGS = json.load(f)
except FileNotFoundError:
    # Provide empty dict if file is missing, allowing defaults to be used
    SETTINGS = {}
except Exception as e:
    print(f"Error loading settings.json: {e}", file=sys.stderr)
    SETTINGS = {}

# Constants with sensible defaults derived from SETTINGS
WINDOW_WIDTH = SETTINGS.get("WINDOW_WIDTH", 800)
WINDOW_HEIGHT = SETTINGS.get("WINDOW_HEIGHT", 600)
CELL_SIZE = SETTINGS.get("CELL_SIZE", 30)
FPS = SETTINGS.get("FPS", 60)
BOARD_WIDTH = SETTINGS.get("BOARD_WIDTH", 10)
BOARD_HEIGHT = SETTINGS.get("BOARD_HEIGHT", 20)
DROP_SPEED = SETTINGS.get("DROP_SPEED", 1000)  # milliseconds
PAUSE_KEY = SETTINGS.get("PAUSE_KEY", "p")
LEFT_KEY = SETTINGS.get("LEFT_KEY", "a")
RIGHT_KEY = SETTINGS.get("RIGHT_KEY", "d")
DOWN_KEY = SETTINGS.get("DOWN_KEY", "s")
ROTATE_KEY = SETTINGS.get("ROTATE_KEY", "w")

# COLORS dictionary (hardcoded, DO NOT fetch from SETTINGS)
COLORS = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "CYAN": (0, 255, 255),
    "MAGENTA": (255, 0, 255),
    "YELLOW": (255, 255, 0),
    # Add more colors as needed
}

# Export symbols
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