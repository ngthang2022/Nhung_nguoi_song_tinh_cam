import pygame
import sys

from scenes.main_menu_scene import MainMenuScene
from scenes.intro_scene import IntroScene
from scenes.map_scene import MapScene
from scenes.quiz_scene import QuizScene

WIDTH, HEIGHT = 1200, 800

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Les Horloges Muettes")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        # Bắt đầu bằng màn hình Menu
        self.run_scene(MainMenuScene)

        # Nếu người chơi nhấn PLAY và không thoát game
        if not self.running:
            return

        # Chuyển sang Intro
        self.run_scene(IntroScene)

        # Sau đó là bản đồ và phần quiz
        if not self.running:
            return
        self.run_scene(MapScene)

        if not self.running:
            return
        self.run_scene(QuizScene)

        pygame.quit()
        sys.exit()

    def run_scene(self, SceneClass):
        print(f"▶ Đang chạy scene: {SceneClass.__name__}")
        scene = SceneClass(self)
        scene.run()

if __name__ == "__main__":
    Game().run()
