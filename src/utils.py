# src/utils.py

def get_piece_color(piece_id):
    """
    Return the RGB color for a given tetromino piece ID.
    IDs correspond to the standard tetrominoes:
    1 - I (Green)
    2 - J (Blue)
    3 - L (Yellow)
    4 - O (Magenta)
    5 - S (Cyan)
    6 - T (Red)
    7 - Z (Orange)
    """
    colors = {
        1: (0, 255, 0),    # I
        2: (0, 0, 255),    # J
        3: (255, 255, 0),  # L
        4: (255, 0, 255),  # O
        5: (0, 255, 255),  # S
        6: (255, 0, 0),    # T
        7: (255, 165, 0),  # Z
    }
    return colors.get(piece_id, (255, 255, 255))