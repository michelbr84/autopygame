import pygame
import sys
from src.settings import *
from src.game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((SETTINGS['SCREEN_WIDTH'], SETTINGS['SCREEN_HEIGHT']))
    pygame.display.set_caption('Tetris Clone')
    clock = pygame.time.Clock()

    # Load assets
    background = pygame.image.load('assets/images/background.png').convert()
    tile_image = pygame.image.load('assets/images/tile.png').convert()
    piece_image = pygame.image.load('assets/images/piece.png').convert_alpha()
    sounds = {
        'line_clear': pygame.mixer.Sound('assets/sounds/line_clear.wav'),
        'rotate': pygame.mixer.Sound('assets/sounds/rotate.wav'),
        'drop': pygame.mixer.Sound('assets/sounds/drop.wav'),
        'game_over': pygame.mixer.Sound('assets/sounds/game_over.wav')
    }

    game = Game(screen, background, tile_image, piece_image, sounds)
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                game.handle_event(event)
        game.update()
        game.draw()
        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()