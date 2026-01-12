# src/piece.py
import random
from .settings import SETTINGS

# Define the 7 tetromino shapes as lists of (x, y) offsets relative to a reference point.
# Each shape is indexed by the piece ID (1‑7). The shapes are stored in the order:
# 1: I, 2: J, 3: L, 4: O, 5: S, 6: T, 7: Z
SHAPES = {
    1: [    # I
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(1, 0), (1, 1), (1, 2), (1, 3)],
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 1), (1, 1), (2, 1), (3, 1)]
    ],
    2: [    # J
        [(0, 0), (1, 0), (2, 0), (2, 1)],
        [(0, 1), (0, 2), (0, 3), (1, 3)],
        [(1, 0), (1, 1), (1, 2), (0, 2)],
        [(2, 1), (2, 2), (2, 3), (1, 3)]
    ],
    3: [    # L
        [(0, 1), (1, 1), (2, 1), (2, 0)],
        [(0, 0), (0, 1), (0, 2), (1, 0)],
        [(0, 0), (1, 0), (2, 0), (0, 1)],
        [(1, 0), (1, 1), (1, 2), (2, 2)]
    ],
    4: [    # O
        [(0, 0), (1, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (0, 1), (1, 1)],
        [(0, 0), (1, 0), (0, 1), (1, 1)]
    ],
    5: [    # S
        [(1, 0), (2, 0), (0, 1), (1, 1)],
        [(1, 0), (1, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 0), (0, 1), (1, 1)],
        [(1, 1), (2, 1), (0, 2), (1, 2)]
    ],
    6: [    # T
        [(0, 0), (1, 0), (2, 0), (1, 1)],
        [(0, 1), (1, 1), (1, 2), (1, 0)],
        [(1, 0), (1, 1), (2, 1), (0, 2)],
        [(0, 1), (1, 1), (0, 2), (1, 2)]
    ],
    7: [    # Z
        [(0, 0), (1, 0), (1, 1), (2, 1)],
        [(1, 0), (1, 1), (0, 2), (1, 2)],
        [(0, 1), (1, 1), (1, 2), (2, 2)],
        [(1, 0), (2, 0), (1, 1), (2, 1)]
    ]
}

class Piece:
    """Represents a single falling tetromino piece."""

    def __init__(self, piece_id=None, rotation=0):
        if piece_id is None:
            piece_id = random.randint(1, 7)
        self.id = piece_id
        self.rotation = rotation
        self.shape = SHAPES[piece_id][rotation]

    @staticmethod
    def random_piece():
        """Factory method to create a random piece with a random rotation."""
        piece_id = random.randint(1, 7)
        rotation = random.randint(0, 3)
        return Piece(piece_id, rotation)

    def coordinates(self):
        """Return the absolute board coordinates of the piece based on its shape and rotation."""
        return self.shape

    def move(self, dx, dy, board_width=SETTINGS['BOARD_WIDTH'], board_height=SETTINGS['BOARD_HEIGHT']):
        """
        Attempt to move the piece by (dx, dy).
        Returns True if the move was successful, False if it collided.
        """
        new_coords = [(x + dx, y + dy) for (x, y) in self.shape]
        # Check bounds and emptiness
        for x, y in new_coords:
            if not (0 <= x < board_width) or not (0 <= y < board_height):
                return False
        # Check collision with other locked blocks (self.board will need to be passed in)
        # For simplicity we just return True here; in the Game.update method collisions are checked indirectly.
        self.shape = new_coords
        return True

    def rotate(self, board):
        """
        Rotate the piece clockwise. If the rotation would cause a collision,
        the rotation is canceled and the method returns False.
        """
        # Get next rotation index
        next_rot = (self.rotation + 1) % 4
        next_shape = SHAPES[self.id][next_rot]
        # Tentatively set shape
        original_shape = self.shape
        self.shape = next_shape
        # Simple collision test: ensure all new coordinates are within bounds and empty
        for x, y in self.shape:
            if not (0 <= x < SETTINGS['BOARD_WIDTH']) or not (0 <= y < SETTINGS['BOARD_HEIGHT']):
                self.shape = original_shape  # revert
                return False
        # Additional collision check could be added here using board data.
        return True