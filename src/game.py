import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings['SCREEN_WIDTH'], settings['SCREEN_HEIGHT']))
        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def update(self):
        pass

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(settings.get('FPS', 60))

if __name__ == "__main__":
    Game().run()