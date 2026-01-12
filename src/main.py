import pygame
from src.settings import SETTINGS
from src.game import Game

def main():
    # Create the screen using the width and height from settings
    screen = pygame.display.set_mode((SETTINGS['SCREEN_WIDTH'], SETTINGS['SCREEN_HEIGHT']))
    pygame.display.set_caption("Tetris-Style Game")
    
    # Instantiate the game with the settings dictionary
    game = Game(SETTINGS)
    
    # Start the game loop (assuming Game.run() handles the loop)
    game.run()

if __name__ == '__main__':
    main()