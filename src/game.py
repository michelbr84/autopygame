import pygame
from .board import Board
from .piece import Piece
from . import utils

class Game:
    def __init__(self, settings):
        self.settings = settings
        self.board = Board(settings)
        self.clock = pygame.time.Clock()
        self.active_piece = None
        self.falling = False
        self.create_new_piece()

    def create_new_piece(self):
        # Instantiate a new piece (random shape & color) and place it at top center
        self.active_piece = Piece(self.settings)
        self.active_piece.x = self.settings['BOARD_WIDTH'] // 2 - len(self.active_piece.shape[0]) // 2
        self.active_piece.y = 0
        self.falling = True

    def update(self):
        if self.falling:
            if utils.time_to_drop(self.clock.get_rawtime(), self.settings.get('DROP_SPEED', 500)):
                # Try to move piece down one cell
                self.active_piece.move(0, 0, 1)
                # Check if new position is still valid
                if not self.board.is_valid_position(self.active_piece.get_shape(), self.active_piece.x, self.active_piece.y):
                    # Revert movement
                    self.active_piece.move(0, 0, -1)
                    # Lock the piece, clear lines, and create a new piece
                    self.board.lock_piece(self.active_piece)
                    self.board.clear_lines()
                    self.create_new_piece()
        utils.handle_input(self)

    def draw(self, surface):
        # Draw all locked pieces
        self.board.draw(surface)
        # Draw the currently falling piece
        self.active_piece.draw(surface)