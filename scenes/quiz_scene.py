import pygame
import sys
import os

pygame.init()
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎮 Quiz Game")

# Fonts
FONT = pygame.font.SysFont("assets/FONT.ttf", 30)
BIG_FONT = pygame.font.SysFont("assets/FONT.ttf", 50)
CLOCK = pygame.time.Clock()

# Màu sắc theo yêu cầu
DARK_BLUE = (0, 9, 87)        
MID_BLUE = (52, 76, 183)      
LIGHT_BLUE = (57, 91, 80)
YELLOW = (255, 235, 0)      
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (31, 47, 22)
GREEN = (146, 175, 215) 
RED = (230, 100, 100)
BLUE = (100, 170, 255)

# Nền
bg_image = pygame.image.load(os.path.join("assets", "soft_gradient_bg.jpg"))
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

# Câu hỏi không randomquestions = [
questions = [
    {
        "question": "Le trouble de stress post-traumatique (TSPT) survient généralement après :",
        "choices": [
            "Un rêve étrange",
            "Une blessure physique légère",
            "Une expérience extrêmement douloureuse ou terrifiante",
            "Un événement joyeux et inattendu"
        ],
        "answer": 2
    },
    {
        "question": "Pourquoi certains anciens combattants comme M. Philippe sont-ils souvent incompris ou stigmatisés dans la société ?",
        "choices": [
            "Parce qu'ils refusent de parler de leur passé",
            "Parce que la communauté manque de connaissances sur les traumatismes psychologiques",
            "Parce qu'ils vivent isolés",
            "Parce qu'ils sont âgés et excentriques"
        ],
        "answer": 1
    },
    {
        "question": "Certaines personnes dans la ville pensent que M. Philippe 'fait semblant'. Laquelle des affirmations suivantes est vraie à propos du TSPT ?",
        "choices": [
            "Le TSPT est une faiblesse mentale, il suffit de penser positivement pour guérir",
            "Le TSPT ne survient que juste après un événement traumatisant et ne peut pas durer des années",
            "Le TSPT est un véritable trouble psychologique, pouvant affecter les émotions, la mémoire et le comportement",
            "Les anciens soldats souffrent rarement de TSPT car ils sont habitués aux traumatismes"
        ],
        "answer": 2
    },
    {
        "question": "Que représente l'ODD 16 ?",
        "choices": [
            "La technologie verte",
            "L'éducation mondiale",
            "La paix, la justice et des institutions efficaces",
            "Le tourisme durable"
        ],
        "answer": 2
    },
    {
        "question": "Dans le contexte de l'ODD 16, laquelle des actions suivantes ne contribue pas à construire une société pacifique et équitable ?",
        "choices": [
            "Encourager le dialogue entre les générations",
            "Exclure les personnes atteintes de troubles psychologiques",
            "Respecter la vérité et écouter les personnes vulnérables",
            "Réduire la stigmatisation dans la communauté"
        ],
        "answer": 1
    },
    {
        "question": "Selon l'esprit de l'ODD 16, que devrait faire une communauté lorsqu'une personne vit isolée en raison d'un traumatisme ?",
        "choices": [
            "L'ignorer pour éviter les problèmes",
            "Chercher à créer des liens, l'écouter et l'aider à se réintégrer",
            "La confier aux autorités compétentes",
            "L'utiliser comme exemple pour avertir les autres"
        ],
        "answer": 1
    },
    {
        "question": "Quel comportement reflète véritablement l'esprit de l'ODD 16 ?",
        "choices": [
            "Garder le silence face à l'injustice",
            "Juger les autres uniquement sur leur apparence",
            "Propager des rumeurs sur les autres",
            "Créer un espace sûr où chacun peut s'exprimer et être écouté"
        ],
        "answer": 3
    },
    {
        "question": "Pourquoi juger une personne uniquement sur des rumeurs ou son passé va-t-il à l'encontre de l'esprit de l'ODD 16 ?",
        "choices": [
            "Parce que cela aide la société à se protéger contre les dangers potentiels",
            "Parce que chacun a droit au respect et à un jugement équitable, sans préjugés",
            "Parce que seuls les proches peuvent juger une personne correctement",
            "Parce que le passé se répète toujours et ne peut pas être changé"
        ],
        "answer": 1
    }
]


# Trạng thái game
current_q = 0
correct = 0
selected_choice = None
show_result = False
result_time = 0
game_state = "playing"

# Typewriter
typed_text = ""
type_index = 0
type_time = 0
TYPE_SPEED = 30  # ms per char

def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""
    
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
    return lines

def draw_question(q, selected=None, show_result=False):
    global typed_text
    screen.blit(bg_image, (0, 0))

    # Khung câu hỏi
    question_box = pygame.Rect(100, 80, WIDTH - 200, 140)
    pygame.draw.rect(screen, (197, 209, 235), question_box, border_radius=30)
    pygame.draw.rect(screen, (128, 128, 128), question_box, 5, border_radius=30)

    # Hiển thị câu hỏi (có xuống dòng)
    lines = wrap_text(typed_text, FONT, question_box.width - 40)
    for i, line in enumerate(lines):
        text_surface = FONT.render(line, True, BLACK)
        screen.blit(text_surface, (question_box.x + 20, question_box.y + 20 + i * 35))

    # Hiển thị các lựa chọn (có xuống dòng)
    for i, choice in enumerate(q["choices"]):
        rect = pygame.Rect(130, 260 + i * 100, 980, 80)
        color = YELLOW
        if show_result:
            if i == q["answer"]:
                color = (57, 91, 80)  # Đúng thì xanh lá
            elif i == selected:
                color = RED          # Sai thì đỏ
        elif i == selected:
            color = BLUE
        elif rect.collidepoint(pygame.mouse.get_pos()):
            color = LIGHT_BLUE

        pygame.draw.rect(screen, color, rect, border_radius=15)
        pygame.draw.rect(screen, (128, 128, 128), rect, 4, border_radius=15)

        # Dòng xuống dòng cho mỗi lựa chọn
        choice_lines = wrap_text(choice, FONT, rect.width - 40)
        for j, line in enumerate(choice_lines):
            text_surface = FONT.render(line, True, BLACK)
            screen.blit(text_surface, (rect.x + 20, rect.y + 10 + j * 25))

    # Hiển thị số câu đúng
    progress_text = FONT.render(f"{correct} correct / 8", True, LIGHT_BLUE)
    screen.blit(progress_text, (20, 20))


def get_choice(pos):
    for i in range(4):
        rect = pygame.Rect(200, 260 + i * 100, 800, 70)
        if rect.collidepoint(pos):
            return i
    return None

def draw_end_screen(result):
    screen.blit(bg_image, (0, 0))
    msg = "🎉 Bạn đã thắng!" if result == "win" else "Vous avez perdu. Il vous faut au moins 6/8 de bonnes réponses."
    label = BIG_FONT.render(msg, True, YELLOW)
    screen.blit(label, (WIDTH//2 - label.get_width()//2, 250))
    retry_btn = pygame.Rect(WIDTH//2 - 120, 400, 240, 70)
    pygame.draw.rect(screen, LIGHT_BLUE, retry_btn, border_radius=6)
    pygame.draw.rect(screen, BLACK, retry_btn, 4, border_radius=6)
    text = FONT.render("Chơi lại", True, BLACK)
    screen.blit(text, (retry_btn.x + 70, retry_btn.y + 20))
    return retry_btn

def reset_game():
    global current_q, correct, selected_choice, show_result, result_time, game_state
    global typed_text, type_index
    current_q = 0
    correct = 0
    selected_choice = None
    show_result = False
    result_time = 0
    typed_text = ""
    type_index = 0
    game_state = "playing"

# Main loop
running = True
while running:
    if game_state == "playing":
        draw_question(questions[current_q], selected_choice, show_result)
        # Hiệu ứng typewriter
        if not show_result:
            full_text = questions[current_q]["question"]
            if type_index < len(full_text):
                now = pygame.time.get_ticks()
                if now - type_time > TYPE_SPEED:
                    typed_text += full_text[type_index]
                    type_index += 1
                    type_time = now

    elif game_state in ["win", "lose"]:
        retry_btn = draw_end_screen(game_state)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "playing" and not show_result:
                selected = get_choice(event.pos)
                if selected is not None:
                    selected_choice = selected
                    show_result = True
                    result_time = pygame.time.get_ticks()
                    if selected == questions[current_q]["answer"]:
                        correct += 1
            elif game_state in ["win", "lose"]:
                if retry_btn.collidepoint(event.pos):
                    reset_game()

    if show_result and pygame.time.get_ticks() - result_time > 1200:
        current_q += 1
        selected_choice = None
        show_result = False
        typed_text = ""
        type_index = 0
        if current_q >= len(questions):
            game_state = "win" if correct >= 6 else "lose"

    CLOCK.tick(60)

pygame.quit()
sys.exit()
