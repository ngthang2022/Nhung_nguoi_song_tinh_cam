import pygame

class DialogBox:
    def __init__(self, screen_width, screen_height, font, box_height=150, padding=20, text_speed=50):
        self.rect = pygame.Rect(0, screen_height - box_height, screen_width, box_height)
        self.bg_color = (30, 30, 30, 220)
        self.border_color = (200, 200, 200)
        
        self.padding = padding
        self.font = font
        self.text_speed = text_speed  # ký tự/giây
        
        self.full_text = ""       # đoạn text đầy đủ
        self.displayed_text = ""  # đoạn text đang hiển thị (gõ từng ký tự)
        
        self.timer = 0
        self.finished = True      # đã gõ xong toàn bộ đoạn

    def set_text(self, text):
        """Thiết lập đoạn text mới để bắt đầu hiện theo kiểu typing style"""
        self.full_text = text
        self.displayed_text = ""
        self.timer = 0
        self.finished = False

    def update(self, dt):
        """Cập nhật trạng thái hiển thị ký tự theo thời gian dt (giây)"""
        if self.finished:
            return
        
        self.timer += dt
        chars_to_show = int(self.timer * self.text_speed)
        
        if chars_to_show >= len(self.full_text):
            chars_to_show = len(self.full_text)
            self.finished = True
        
        self.displayed_text = self.full_text[:chars_to_show]

    def draw(self, surface):
        """Vẽ hộp thoại và text lên bề mặt surface"""
        s = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        s.fill(self.bg_color)
        surface.blit(s, (self.rect.x, self.rect.y))
        
        pygame.draw.rect(surface, self.border_color, self.rect, 10)
        
        words = self.displayed_text.split(' ')
        lines = []
        line = ""
        max_width = self.rect.width - 2 * self.padding
        
        for word in words:
            test_line = line + word + " "
            w, _ = self.font.size(test_line)
            if w > max_width:
                lines.append(line)
                line = word + " "
            else:
                line = test_line
        lines.append(line)
        
        y = self.rect.y + self.padding
        for line in lines:
            text_surface = self.font.render(line, True, (255, 255, 255))
            surface.blit(text_surface, (self.rect.x + self.padding, y))
            y += self.font.get_height() + 5

    def skip_or_next(self):
        """
        Nếu đang gõ dở thì hiện hết ngay.
        Nếu đã xong thì trả về True để thông báo sẵn sàng chuyển đoạn tiếp theo.
        """
        if not self.finished:
            self.displayed_text = self.full_text
            self.finished = True
            return False  # Chưa chuyển đoạn, chỉ hiện toàn bộ
        return True  # Sẵn sàng chuyển đoạn mới
