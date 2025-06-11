import pygame

class DialogBox:
    def __init__(self, screen_width, screen_height, font, box_height=150, padding=20, text_speed=50):
        # Vị trí và kích thước hộp thoại nằm dưới cùng màn hình
        self.rect = pygame.Rect(0, screen_height - box_height, screen_width, box_height)
        
        # Màu nền (có alpha để bán trong suốt)
        self.bg_color = (30, 30, 30, 220)
        self.border_color = (200, 200, 200)
        
        self.padding = padding
        self.font = font
        self.text_speed = text_speed  # ký tự/giây
        
        # Text hiện tại đang hiển thị (typing)
        self.full_text = ""       # đoạn text đầy đủ
        self.displayed_text = ""  # đoạn text đang hiển thị (gõ từng ký tự)
        
        self.timer = 0
        self.finished = True      # ban đầu box trống, chưa có text để hiển thị
    
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
        # Vẽ nền hộp thoại có alpha (bán trong suốt)
        s = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        s.fill(self.bg_color)
        surface.blit(s, (self.rect.x, self.rect.y))
        
        # Vẽ viền hộp thoại
        pygame.draw.rect(surface, self.border_color, self.rect, 10)
        
        # Tách đoạn displayed_text thành các dòng sao cho vừa khung
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
        
        # Vẽ từng dòng chữ
        y = self.rect.y + self.padding
        for line in lines:
            text_surface = self.font.render(line, True, (255, 255, 255))
            surface.blit(text_surface, (self.rect.x + self.padding, y))
            y += self.font.get_height() + 5
    
