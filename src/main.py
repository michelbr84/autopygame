import pygame
from src.settings import SETTINGS

def main():
    pygame.init()
    # Create the screen using settings for width and height
    screen = pygame.display.set_mode((SETTINGS['SCREEN_WIDTH'], SETTINGS['SCREEN_HEIGHT']))
    pygame.display.set_caption(SETTINGS.get('GAME_TITLE', 'Game'))

    # Import and instantiate the main game class (assumed to be in src.game)
    from src.game import Game
    game = Game(screen)
    game.run()

if __name__ == '__main__':
    main()