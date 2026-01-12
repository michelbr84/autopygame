import pygame
import sys

class Game:
    def __init__(self, settings):
        """
        Initialize pygame and create the game screen based on settings.
        Expected settings keys: SCREEN_WIDTH, SCREEN_HEIGHT, FPS (and optionally others).
        """
        self.settings = settings
        pygame.init()
        self.screen = pygame.display.set_mode(
            (settings['SCREEN_WIDTH'], settings['SCREEN_HEIGHT'])
        )
        self.clock = pygame.time.Clock()

    def run(self):
        """
        Main game loop:
          - Process events (including QUIT to exit)
          - Update game state (placeholder)
          - Draw / render (placeholder)
          - Tick the clock at the target FPS
        """
        # Main loop
        while True:
            # Process events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Update game state (placeholder - override or extend in subclasses)
            # self.update()

            # Draw / render (placeholder - override or extend in subclasses)
            # self.draw()

            pygame.display.flip()
            self.clock.tick(self.settings['FPS'])


# Optional: simple direct execution for testing
if __name__ == '__main__':
    SETTINGS = {
        'SCREEN_WIDTH': 800,
        'SCREEN_HEIGHT': 600,
        'FPS': 60
    }
    game = Game(SETTINGS)
    game.run()