import pygame
from pygame.locals import *
import random

WINDOW_SYZE = (400, 400)
PIXEL_SYZE = (10)


def collision(pos1, pos2):
    return pos1 == pos2


def off_limits(pos):
    if 0 <= pos[0] < WINDOW_SYZE[0] and 0 <= pos[1] < WINDOW_SYZE[1]:
        return False
    else:
        return True


def random_on_grid():
    x = random.randint(0, WINDOW_SYZE[0])
    y = random.randint(0, WINDOW_SYZE[1])
    return x // PIXEL_SYZE * PIXEL_SYZE, y // PIXEL_SYZE * PIXEL_SYZE


# Definindo a tela
pygame.init()
screen = pygame.display.set_mode(WINDOW_SYZE)
pygame.display.set_caption('Jogo da Cobrinha')

# Defindo posição da cobrinha e tambem o tamanho dela
snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((PIXEL_SYZE, PIXEL_SYZE))
snake_surface.fill((43, 114, 25))
snake_direction = K_LEFT

egg_surface = pygame.Surface((PIXEL_SYZE, PIXEL_SYZE))
egg_surface.fill([240, 181, 141])
egg_pos = random_on_grid()


def restart_game():
    global snake_pos
    global egg_pos
    global snake_direction
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    snake_direction = K_LEFT
    egg_pos = random_on_grid()


# Essa estrutura mantem a tela aberta e tbm torna possivel fechar ela
while True:
    pygame.time.Clock().tick(15)

    screen.fill([51, 35, 27])
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key

    screen.blit(egg_surface, egg_pos)
    if collision(egg_pos, snake_pos[0]):
        snake_pos.append((-10, -10))
        egg_pos = random_on_grid()

    for pos in snake_pos:
        screen.blit(snake_surface, pos)
    try:
        for i in range(len(snake_pos) - 1, 0, -1):
            if collision(snake_pos[0], snake_pos[i]):
                restart_game()
            if i > 0:
                snake_pos[i] = snake_pos[i - 1]
    except:
        restart_game()

    if off_limits(snake_pos[0]):
        restart_game()

    if K_UP == snake_direction:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SYZE)
    elif K_DOWN == snake_direction:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SYZE)
    elif K_LEFT == snake_direction:
        snake_pos[0] = (snake_pos[0][0] - PIXEL_SYZE, snake_pos[0][1])
    elif K_RIGHT == snake_direction:
        snake_pos[0] = (snake_pos[0][0] + PIXEL_SYZE, snake_pos[0][1])

    pygame.display.update()
