import pygame

class MapScene:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.clock = game.clock
        self.running = True
        self.font = pygame.font.SysFont(None, 50)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.game.running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.running = False  # chuyển qua QuizScene

            self.screen.fill((50, 100, 150))
            text = self.font.render("Map Scene - Nhấn ENTER để tiếp tục", True, (255, 255, 255))
            self.screen.blit(text, (300, 350))
            pygame.display.flip()
            self.clock.tick(60)
