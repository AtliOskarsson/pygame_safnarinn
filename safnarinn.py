import pygame
from pygame.locals import *
from random import randint

pygame.init()
pygame.font.init()

window_size = window_width, window_height = 960, 770
window = pygame.display.set_mode(window_size)

pygame.display.set_caption('Safnarinn')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
rainbow = (randint(0, 255), randint(0, 255), randint(0, 255))
myfont = pygame.font.SysFont('Comic Sans MS', 30)

x_position = 420
y_position = 660

x_velocity = 0

window.fill(BLACK)

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                x_velocity = -7
            elif event.key == pygame.K_d:
                x_velocity = 7

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_a:
                x_velocity = 0
            elif event.key == pygame.K_d:
                x_velocity = 0


    x_position += x_velocity

    window.fill(BLUE)
    pygame.draw.rect(window, WHITE, pygame.Rect(x_position, y_position, 90, 15))

    pygame.display.update()
    clock.tick(60)
pygame.quit()

