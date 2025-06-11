import pygame
import sys

from Dialog import DialogBox

# Hàm hiệu ứng fade-in
def fade_in(surface, image, duration=500):
    clock = pygame.time.Clock()
    alpha_img = image.copy()
    for alpha in range(0, 256, 10):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        alpha_img.set_alpha(alpha)
        surface.fill((0, 0, 0))
        surface.blit(alpha_img, (0, 0))
        pygame.display.flip()
        clock.tick(1000 // (duration // 10))

# Khởi tạo Pygame
pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Scene 1")
screen.fill((0, 0, 0))

count = 0
current_image = None
font = pygame.font.Font('assets/FONT.ttf', 28)
dialog = DialogBox(1200, 800, font)
clock = pygame.time.Clock()

# Load ảnh
P1 = [
    pygame.image.load("assets/P1_1.png").convert_alpha(),
    pygame.image.load("assets/P1_2.png").convert_alpha(),
    pygame.image.load("assets/P1_3.png").convert_alpha()
]

P2 = [
    pygame.image.load("assets/P2_1.png").convert_alpha(),
    pygame.image.load("assets/P2_2.png").convert_alpha(),
    pygame.image.load("assets/P2_3.png").convert_alpha()
]

P3 = [
    pygame.image.load("assets/P3_1.png").convert_alpha(),
    pygame.image.load("assets/P3_2.png").convert_alpha(),
    pygame.image.load("assets/P3_3.png").convert_alpha(),
    pygame.image.load("assets/P3_4.png").convert_alpha()
]

# Resize ảnh về khung 1200x800
for i in range(len(P1)):
    P1[i] = pygame.transform.scale(P1[i], (1200, 800))
for i in range(len(P2)):
    P2[i] = pygame.transform.scale(P2[i], (1200, 800))
for i in range(len(P3)):
    P3[i] = pygame.transform.scale(P3[i], (1200, 800))

# Kết hợp tất cả ảnh
all_images = P1 + P2 + P3

# Kịch bản hội thoại (phải khớp số ảnh)
script = [
    "Ong cu nay bi PTSD,kieu v@@@",
    "... ,kinda worry",
    "Minh se kiem ong ta",
    "ArHHHHHHHH, cuu toi",
    "...",
    "Cu oi",
    "heyy",
    ",,",
    "Toi dang nghi gi do...",
    "Cau hieu roi chu?"
]

# Hiển thị ảnh đầu tiên và thoại đầu tiên
current_image = all_images[0]
dialog.set_text(script[0])
fade_in(screen, current_image)

# Vòng lặp chính
while count < len(script):
    dt = clock.tick(60) / 5000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            count += 1
            if count < len(script) and count < len(all_images):
                current_image = all_images[count]
                dialog.set_text(script[count])
                fade_in(screen, current_image)
    
    dialog.update(dt)
    dialog.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
