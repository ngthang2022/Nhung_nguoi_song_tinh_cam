import pygame

class MainMenuScene:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.clock = game.clock
        self.running = True
        pygame.font.init()

        # Font pixel
        self.font = pygame.font.Font("assets/Pixel Emulator.otf", 30)

        # Buttons
        self.play_button_rect = pygame.Rect(450, 350, 300, 100)
        self.help_button_rect = pygame.Rect(450, 470, 300, 100)

        # Background & logo
        self.background = pygame.image.load("assets/menu_bg.png").convert()
        self.background = pygame.transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))

        self.logo = pygame.image.load("assets/logo.png").convert_alpha()  # Logo game
        self.logo = pygame.transform.scale(self.logo, (500, 500))
        self.logo_rect = self.logo.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))

        # Fade timing
        self.fade_duration = 2000  # 2 giây
        self.hold_duration = 1000  # giữ thêm 1 giây

    def show_intro_logo(self):
        print("✨ Hiển thị logo game (fade-in)...")
        start_time = pygame.time.get_ticks()
        while True:
            now = pygame.time.get_ticks()
            elapsed = now - start_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.game.running = False
                    return

            self.screen.fill((0, 0, 0))

            if elapsed < self.fade_duration:
                alpha = int(255 * (elapsed / self.fade_duration))
            else:
                alpha = 255

            logo_surface = self.logo.copy()
            logo_surface.set_alpha(alpha)
            self.screen.blit(logo_surface, self.logo_rect)

            pygame.display.flip()
            self.clock.tick(60)

            if elapsed > self.fade_duration + self.hold_duration:
                break

    def run(self):
        self.show_intro_logo()  # 🆕 Gọi hiệu ứng logo trước

        print("▶ MainMenuScene đang chạy...")
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.game.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button_rect.collidepoint(event.pos):
                        print("🟢 Nút PLAY được nhấn")
                        self.running = False
                    elif self.help_button_rect.collidepoint(event.pos):
                        print("🟡 Nút HELP được nhấn")

            # Vẽ nền
            self.screen.blit(self.background, (0, 0))

            # Tiêu đề game
            title = self.font.render("Les Horloges Muettes", True, (0, 0, 0))
            title_rect = title.get_rect(center=(self.screen.get_width() // 2, 150))
            self.screen.blit(title, title_rect)

            # Nút PLAY
            pygame.draw.rect(self.screen, (70, 130, 180), self.play_button_rect, border_radius=12)
            pygame.draw.rect(self.screen, (255, 255, 255), self.play_button_rect, 4, border_radius=12)
            play_text = self.font.render("PLAY", True, (255, 255, 255))
            play_text_rect = play_text.get_rect(center=self.play_button_rect.center)
            self.screen.blit(play_text, play_text_rect)

            # Nút HELP
            pygame.draw.rect(self.screen, (70, 130, 180), self.help_button_rect, border_radius=12)
            pygame.draw.rect(self.screen, (255, 255, 255), self.help_button_rect, 4, border_radius=12)
            help_text = self.font.render("HELP", True, (255, 255, 255))
            help_text_rect = help_text.get_rect(center=self.help_button_rect.center)
            self.screen.blit(help_text, help_text_rect)

            pygame.display.flip()
            self.clock.tick(60)
