# src/settings.py
SETTINGS = {
    'SCREEN_WIDTH': 800,
    'SCREEN_HEIGHT': 600,
    'TILE_SIZE': 30,
    'BOARD_WIDTH': 10,
    'BOARD_HEIGHT': 20,
    'FPS': 60,
    'BACKGROUND_COLOR': (0, 0, 0),
    'COLORS': {
        'WHITE': (255, 255, 255),
        'BLACK': (0, 0, 0),
        'GRAY': (128, 128, 128),
        'RED': (255, 0, 0),
        'GREEN': (0, 255, 0),
        'BLUE': (0, 0, 255),
        'YELLOW': (255, 255, 0),
        'CYAN': (0, 255, 255),
        'MAGENTA': (255, 0, 255),
        'ORANGE': (255, 165, 0),
    },
    'TILE_COLORS': [
        (0, 0, 0),          # Empty (background)
        (0, 255, 0),        # I - Green
        (0, 0, 255),        # J - Blue
        (255, 255, 0),      # L - Yellow
        (255, 0, 255),      # O - Magenta
        (0, 255, 255),      # S - Cyan
        (255, 0, 0),        # T - Red
        (255, 165, 0),      # Z - Orange
    ],
}