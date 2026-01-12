import pygame
import sys

class Game:
    def __init__(self, settings):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (settings['SCREEN_WIDTH'], settings['SCREEN_HEIGHT'])
        )
        self.settings = settings
        self.clock = pygame.time.Clock()

    def update(self):
        # Placeholder for game logic updates
        pass

    def draw(self):
        # Placeholder for drawing
        pass

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.settings['FPS'])


if __name__ == "__main__":
    settings = {
        'SCREEN_WIDTH': 800,
        'SCREEN_HEIGHT': 600,
        'FPS': 60,
    }
    game = Game(settings)
    game.run()