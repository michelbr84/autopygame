# src/board.py
import pygame
from src.settings import SETTINGS

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # 2D grid where 0 represents an empty cell
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def is_empty(self, x, y):
        return 0 <= x < self.width and y < self.height and self.grid[y][x] == 0

    def lock_piece(self, piece):
        """Lock the current piece into the board grid."""
        for x, y in piece.coordinates():
            if 0 <= x < self.width and y < self.height:
                self.grid[y][x] = piece.id + 1  # store piece identifier (1‑7)

    def get_color(self, piece_id):
        """Return a color for a given piece identifier."""
        # Colors align with SETTINGS['COLORS'] (1‑based indexing)
        colors = [
            (0, 0, 0),  # placeholder for index 0 (unused)
        ] + [SETTINGS['COLORS'][name] for name in ['RED', 'GREEN', 'BLUE', 'YELLOW', 'CYAN', 'MAGENTA', 'ORANGE']]
        return colors[piece_id]

    def clear_lines(self):
        """Remove all completed lines and return the number of lines cleared."""
        lines_cleared = 0
        new_grid = []
        for row in self.grid:
            if all(cell != 0 for cell in row):
                lines_cleared += 1
            else:
                new_grid.append(row)
        # Insert empty rows at the top for the cleared lines
        for _ in range(lines_cleared):
            new_grid.insert(0, [0 for _ in range(self.width)])
        self.grid = new_grid
        return lines_cleared

    def is_game_over(self):
        """Check if the board is full in the top row (game over condition)."""
        return any(self.grid[0][x] != 0 for x in range(self.width))

    def draw(self, surface, tile_image):
        """Draw the board onto the given surface using the provided tile image."""
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell != 0:
                    # Draw a colored rectangle for the locked block
                    color = self.get_color(cell)
                    pygame.draw.rect(
                        surface,
                        color,
                        (x * SETTINGS['TILE_SIZE'],
                         y * SETTINGS['TILE_SIZE'],
                         SETTINGS['TILE_SIZE'],
                         SETTINGS['TILE_SIZE'])
                    )
                    # Optionally overlay the tile image
                    # surface.blit(tile_image, (x * SETTINGS['TILE_SIZE'], y * SETTINGS['TILE_SIZE']))