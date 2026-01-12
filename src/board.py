import pygame

class Board:
    def __init__(self, settings):
        self.settings = settings
        self.grid = [[0 for _ in range(settings['BOARD_WIDTH'])] for _ in range(settings['BOARD_HEIGHT'])]
        self.locked_shapes = {}

    def is_valid_position(self, shape, x, y):
        """Check if the given shape at (x, y) stays inside the board boundaries."""
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

    def lock_piece(self, piece):
        """Lock the current piece into the grid."""
        for row_idx, row in enumerate(piece.get_shape()):
            for col_idx, val in enumerate(row):
                if val:
                    grid_x = piece.x + col_idx
                    grid_y = piece.y + row_idx
                    if 0 <= grid_x < self.settings['BOARD_WIDTH'] and 0 <= grid_y < self.settings['BOARD_HEIGHT']:
                        self.grid[grid_y][grid_x] = piece.get_color()

    def clear_lines(self):
        """Remove any completely filled rows and shift everything down."""
        new_grid = []
        lines_cleared = 0
        for row in self.grid:
            if not self._is_full_row(row):
                new_grid.append(row)
            else:
                lines_cleared += 1
        # Add empty rows at the top
        while len(new_grid) < len(self.grid):
            new_grid.insert(0, [0 for _ in range(self.settings['BOARD_WIDTH'])])
        self.grid = new_grid

    def _is_full_row(self, row):
        return all(row)

    def draw(self, surface):
        """Draw the board grid and any locked pieces."""
        cell_size = self.settings['CELL_SIZE']
        for y, row in enumerate(self.grid):
            for x, color in enumerate(row):
                if color:
                    pygame.draw.rect(
                        surface,
                        color,
                        (x * cell_size, y * cell_size, cell_size, cell_size)
                    )