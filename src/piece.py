from . import utils
import pygame

class Piece:
    def __init__(self, settings):
        self.settings = settings
        self.type = utils.random_shape()
        self.color = utils.random_color()
        self.shape = utils.get_shape(self.type)
        self.x = settings['BOARD_WIDTH'] // 2 - len(self.shape[0]) // 2
        self.y = 0

    def get_shape(self):
        return self.shape

    def get_color(self):
        return self.color

    def move(self, dx, dy, steps=1):
        self.x += dx * steps
        self.y += dy * steps

    def rotate(self):
        # Rotate the shape 90 degrees clockwise
        rotated = [list(row) for row in zip(*self.shape[::-1])]
        self.shape = rotated

        # Adjust position after rotation to keep it on the board when possible
        while not self._is_valid_position(self.shape, self.x, self.y):
            # Try shifting left
            if self._is_valid_position(self.shape, self.x - 1, self.y):
                self.x -= 1
                break
            # Try shifting right
            if self._is_valid_position(self.shape, self.x + 1, self.y):
                self.x += 1
                break
            # If neither works, stop rotating
            break

    def _is_valid_position(self, shape, x, y):
        """Check whether the given shape at (x, y) lies completely within the board."""
        board_width = self.settings['BOARD_WIDTH']
        board_height = self.settings['BOARD_HEIGHT']
        for row_idx, row in enumerate(shape):
            for col_idx, val in enumerate(row):
                if val:
                    new_x = x + col_idx
                    new_y = y + row_idx
                    if new_x < 0 or new_x >= board_width:
                        return False
                    if new_y < 0 or new_y >= board_height:
                        return False
        return True

    def draw(self, surface):
        """Draw the piece on the given surface."""
        cell_size = self.settings['CELL_SIZE']
        for row_idx, row in enumerate(self.shape):
            for col_idx, val in enumerate(row):
                if val:
                    rect = pygame.Rect(
                        (self.x + col_idx) * cell_size,
                        (self.y + row_idx) * cell_size,
                        cell_size,
                        cell_size
                    )
                    pygame.draw.rect(surface, self.color, rect)