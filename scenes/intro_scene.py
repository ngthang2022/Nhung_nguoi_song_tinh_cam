import pygame
import sys
from scenes.Dialog import DialogBox

class IntroScene:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.clock = game.clock
        self.running = True

        self.count = 0
        self.font = pygame.font.Font('assets/Minecraftia-Regular.ttf', 28)
        self.dialog = DialogBox(1200, 800, self.font)
        self.load_images()
        self.dialog.set_text(self.script[0])
        self.fade_in(self.screen, self.current_image)

    def load_images(self):
        P1 = [pygame.image.load(f"assets/P1_{i+1}.png").convert_alpha() for i in range(7)]
        P2 = [pygame.image.load(f"assets/P2_{i+1}.png").convert_alpha() for i in range(3)]
        P3 = [pygame.image.load(f"assets/P3_{i+1}.png").convert_alpha() for i in range(4)]

        for lst in [P1, P2, P3]:
            for i in range(len(lst)):
                lst[i] = pygame.transform.scale(lst[i], (1200, 800))

        self.all_images = P1 + P2 + P3

        # ✨ Chèn lại ảnh frame 1 cho đoạn thoại phụ thứ 2 (giữ nguyên hình nền)
        self.all_images.insert(1, self.all_images[0])

        # 📝 Kịch bản hội thoại (frame 0 và 1 dùng chung hình ảnh)
        self.script = [
            "C'est Léo, un lycéen passionné de philosophie et sensible aux enjeux sociaux",  # frame 0
            "Récemment, il a perdu des points de comportement à l’école parce qu’il était trop absorbé par la lecture de livres sur l’histoire et la guerre",                      # frame 0 (ảnh lặp)
            "... ,kinda worry",                                                              # frame 1
            "Minh se kiem ong ta",
            "ArHHHHHHHH, cuu toi",
            "...",
            "Cu oi",
            "heyy",
            ",,",
            "Toi dang nghi gi do...",
            "Cau hieu roi chu?"
        ]

        self.current_image = self.all_images[0]

    def fade_in(self, surface, image, duration=500):
        clock = pygame.time.Clock()
        alpha_img = image.copy()
        for alpha in range(0, 256, 10):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.game.running = False
            alpha_img.set_alpha(alpha)
            surface.fill((0, 0, 0))
            surface.blit(alpha_img, (0, 0))
            pygame.display.flip()
            clock.tick(1000 // (duration // 10))

    def run(self):
        print("▶ IntroScene đang chạy...")
        while self.running and self.count < len(self.script):
            dt = self.clock.tick(60) / 5000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.game.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.dialog.skip_or_next():
                        self.count += 1
                        if self.count < len(self.script) and self.count < len(self.all_images):
                            self.current_image = self.all_images[self.count]
                            self.current_image.set_alpha(None)  # Reset alpha sau fade_in
                            self.dialog.set_text(self.script[self.count])
                            self.fade_in(self.screen, self.current_image)
                        else:
                            self.running = False  # Hết kịch bản thì thoát scene

            self.dialog.update(dt)
            self.screen.blit(self.current_image, (0, 0))
            self.dialog.draw(self.screen)
            pygame.display.flip()
