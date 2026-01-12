# src/game.py
import pygame
from .settings import SETTINGS
from .board import Board
from .piece import Piece

class Game:
    def __init__(self, screen, background, tile_image, piece_image, sounds):
        self.screen = screen
        self.background = background
        self.tile_image = tile_image
        self.piece_image = piece_image
        self.sounds = sounds

        self.board = Board(SETTINGS['BOARD_WIDTH'], SETTINGS['BOARD_HEIGHT'])
        self.current_piece = None
        self.next_piece = None
        self.fall_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.fall_event, SETTINGS['FALL_SPEED'])

        self.running = True
        self.new_piece()

    def new_piece(self):
        """Create a new current piece and a new next piece."""
        self.current_piece = self.next_piece if self.next_piece else Piece.random_piece()
        self.next_piece = Piece.random_piece()

    def handle_event(self, event):
        """Process user input."""
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.current_piece.move(-1)
            elif event.key == pygame.K_RIGHT:
                self.current_piece.move(1)
            elif event.key == pygame.K_DOWN:
                self.current_piece.move(0, 1)
            elif event.key == pygame.K_UP:
                self.current_piece.rotate()

    def update(self):
        """Update game state: move piece down automatically."""
        for event in pygame.event.get():
            if event.type == self.fall_event:
                if not self.current_piece.move(0, 1):
                    # Piece can't move down → lock it
                    self.board.lock_piece(self.current_piece)
                    self.clear_lines()
                    self.new_piece()
        # If the game is over (new piece collides immediately), you could handle it here.

    def clear_lines(self):
        """Check for completed lines, remove them, and play a sound."""
        lines_cleared = self.board.clear_lines()
        if lines_cleared > 0:
            self.sounds['line_clear'].play()

    def draw(self):
        """Render everything to the screen."""
        self.screen.blit(self.background, (0, 0))

        # Draw the board
        self.board.draw(self.screen, self.tile_image)

        # Draw the falling piece
        self.current_piece.draw(self.screen, self.tile_image)

        pygame.display.flip()