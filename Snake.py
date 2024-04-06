# import modules
import pygame
from pygame.locals import *

pygame.init()

# create blank game window
screen_width = 600
screen_height = 600

# create game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake')

# define game variables
cell_size = 10
# 1 is up, 2 is right, 3 is down, and 4 is left
direction = 1

# create snake
snake_pos = [[int(screen_width / 2), int(screen_height / 2)],
             [int(screen_width / 2), int(screen_height / 2) + cell_size],
             [int(screen_width / 2), int(screen_height / 2) + cell_size * 2],
             [int(screen_width / 2), int(screen_height / 2) + cell_size * 3]]

# define background colors
bg = (255, 200, 150)
body_inner = (50, 175, 25)
body_outer = (100, 100, 200)
snake_head = (255, 0, 0)

def draw_screen():
    screen.fill(bg)


# setup loop with exit
run = True
while run:

    draw_screen()

    # iterate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3:
                direction = 1
            if event.key == pygame.K_RIGHT and direction != 4:
                direction = 2
            if event.key == pygame.K_DOWN and direction != 1:
                direction = 3
            if event.key == pygame.K_LEFT and direction != 2:
                direction = 4


    # draw snake
    head = 1
    for x in snake_pos:
        if head == 0:
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pygame.draw.rect(screen, body_inner, (x[0] + 1, x[1] + 1, cell_size - 2, cell_size - 2))
        if head == 1:
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pygame.draw.rect(screen, snake_head, (x[0] + 1, x[1] + 1, cell_size - 2, cell_size - 2))
            head = 0

    # update display
    pygame.display.update()

# end game
pygame.quit()
