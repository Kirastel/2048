import sys
import pygame
from logics import *
from database import get_best, cur, insert_result


GAMERS_DB = get_best()

COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 255, 128),
    8: (255, 255, 0),
    16: (255, 235, 255),
    32: (255, 235, 255),
    64: (255, 235, 255),
    128: (255, 235, 255)
}

mas = None
score = None
USERNAME = None
WHITE = (255, 255, 255)
GREY = (130, 130, 130)
BLACK = (0, 0, 0)
BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + MARGIN * 5
HEIGHT = BLOCKS * SIZE_BLOCK + MARGIN * 5 + SIZE_BLOCK
TITLE_REG = pygame.Rect(0, 0, WIDTH, SIZE_BLOCK)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")


def best_score():
    font_head = pygame.font.SysFont('simsun', 30)
    font_gamer = pygame.font.SysFont('simsun', 24)
    text_head = font_head.render(f'Best:', True, BLACK)
    screen.blit(text_head, (220, -5))

    for index, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        s = f'{index + 1}. {name} - {score}'
        text_gamer = font_gamer.render(s, True, BLACK)
        screen.blit(text_gamer, (220, 20 + 25 * index))


def init_const():
    global mas, score
    mas = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    score = 0


    empty = get_emty_list(mas)
    random.shuffle(empty)
    random_num1 = empty.pop()
    random_num2 = empty.pop()
    x1, y1 = get_index_from_number(random_num1)
    x2, y2 = get_index_from_number(random_num2)
    mas = insert_2_or_2(mas, x1, y1)
    mas = insert_2_or_2(mas, x2, y2)
    score = 0


def draw_interface(score):
    pygame.draw.rect(screen, WHITE, TITLE_REG)
    font = pygame.font.SysFont('stxingkai', 70)
    font_score = pygame.font.SysFont('simsun', 48)
    text_score = font.render(f'Счет:  {score} ', True, BLACK)
    screen.blit(text_score, (20, 35))
    best_score()
    for row in range(BLOCKS):
        for column in range(BLOCKS):
            value = mas[row][column]
            text = font.render(f'{value}', True, BLACK)
            w = column * SIZE_BLOCK + (column + 1) * MARGIN
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + SIZE_BLOCK
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCK - font_w) // 2
                text_y = h + (SIZE_BLOCK - font_h) // 2
                screen.blit(text, (text_x, text_y))
    pygame.display.update()


def draw_intro():
    start_img = pygame.image.load('unnamed.png')
    font_start = pygame.font.SysFont('stxingkai', 40)
    welcome_message = 'Добро пожаловать в игру 2048'
    text_start = font_start.render(welcome_message, True, WHITE)
    name = 'Введите имя'
    is_find_name = False
    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == 'Введите имя':
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN and (len(name) > 0 and name != 'Введите имя'):
                    global USERNAME
                    USERNAME = name
                    is_find_name = True
                    break
        screen.fill(BLACK)
        text_name = font_start.render(name, True, WHITE)
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center
        screen.blit(pygame.transform.scale(start_img, (200, 200)), (10, 10))
        screen.blit(text_start, (250, 60))
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill(BLACK)


def draw_GameOver():
    global USERNAME, mas
    font_over = pygame.font.SysFont('stxingkai', 40)
    over_message = f'Игра окончена!'
    score_over = f'Ваш счет {score}  Нажмите ENTER, что - бы начать новую игра \Нажмите ESC, что - бы выйти.'
    text_over = font_over.render(over_message, True, WHITE)
    score_over = font_over.render(score_over, True, WHITE)
    insert_result(USERNAME, score)
    make_desicion = False
    while not make_desicion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    make_desicion = True
                elif event.key == pygame.K_RETURN:
                    USERNAME = None
                    make_desicion =True
        screen.fill(BLACK)
        screen.blit(text_over, (30, 250))
        screen.blit(score_over, (30, 300))
        pygame.display.update()
    screen.fill(BLACK)


def main():
    global score, mas
    draw_interface(score)
    pygame.display.update()
    while is_zero_in_mas(mas) or can_move(mas):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                delta = 0
                if event.key == pygame.K_LEFT:
                    mas, delta = move_left(mas)
                elif event.key == pygame.K_RIGHT:
                    mas, delta = move_right(mas)
                elif event.key == pygame.K_UP:
                    mas, delta= move_up(mas)
                elif event.key == pygame.K_DOWN:
                    mas, delta= move_down(mas)
                score +=  delta
                if is_zero_in_mas(mas):
                    empty = get_emty_list(mas)
                    random.shuffle(empty)
                    random_num = empty.pop()
                    x, y = get_index_from_number(random_num)
                    mas = insert_2_or_2(mas, x, y)
                draw_interface(score)
                pygame.display.update()

while True:
    if USERNAME is None:
        draw_intro()
    main()
    draw_GameOver()
