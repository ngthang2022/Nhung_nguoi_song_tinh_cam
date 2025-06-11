import pygame
import sys

# Import từng scene riêng
from scenes.intro_scene import IntroScene
from scenes.map_scene import MapScene
from scenes.quiz_scene import QuizScene
from scenes.maze_scene import MazeScene
from scenes.timeline_scene import TimelineScene
from scenes.outro_scene import OutroScene

# Cấu hình chung
WIDTH, HEIGHT = 1200, 800
FPS = 60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Horloges Muettes")
        self.clock = pygame.time.Clock()
        self.running = True

        # Các biến trạng thái
        self.collected_items = []
        self.quiz_passed = False
        self.maze_passed = False
        self.timeline_passed = False

    def run(self):
        # Chạy từng scene theo trình tự
        self.run_scene(IntroScene)
        self.run_scene(MapScene)

        # Giả sử sau khi chọn 3 món đồ → chạy 3 minigame:
        self.run_scene(QuizScene)
        self.run_scene(MazeScene)
        self.run_scene(TimelineScene)

        # Kết thúc game
        self.run_scene(OutroScene)

        pygame.quit()
        sys.exit()

    def run_scene(self, SceneClass):
        scene = SceneClass(self)
        scene.run()

if __name__ == "__main__":
    game = Game()
    game.run()
