# import modules
import pygame


import random


pygame.init()

# create blank game window
screen_width = 600
screen_height = 600

# create game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake')

# define game variables
cell_size = 10
direction = 1 # 1 is up, 2 is right, 3 is down, and 4 is left
update_snake = 0
food = [0, 0]
new_food = True
new_piece = [0, 0]
score = 0


# create snake
snake_pos = [[int(screen_width / 2), int(screen_height / 2)],
             [int(screen_width / 2), int(screen_height / 2) + cell_size],
             [int(screen_width / 2), int(screen_height / 2) + cell_size * 2],
             [int(screen_width / 2), int(screen_height / 2) + cell_size * 3]]


# declare font
font = pygame.font.SysFont(None, 40)

# define background colors
bg = (255, 200, 150)
body_inner = (50, 175, 25)
body_outer = (100, 100, 200)
snake_head = (255, 0, 0)
food_col = (200, 50, 50)
score_col = (0, 0, 255)

def draw_screen():
    screen.fill(bg)


def draw_score():
    score_txt = 'Score:' + str(score)
    score_img = font.render(score_txt, True, score_col)
    screen.blit(score_img, (0, 0))


# setup loop with exit
run = True
while run:

    draw_screen()
    draw_score()

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


    #create food
    if new_food == True:
        new_food = False
        # noinspection PyTypeChecker
        food[0] = cell_size * random.randint(0, (screen_width // cell_size) - 1)
        # noinspection PyTypeChecker
        food[1] = cell_size * random.randint(0, (screen_height // cell_size) - 1)


    #draw food
    pygame.draw.rect(screen, food_col, (food[0], food[1], cell_size, cell_size))


    # check if food has been eaten
    if snake_pos[0] == food:
        new_food = True
        #create new snake segment
        new_piece = list(snake_pos[-1])
        if direction == 1:
            new_piece[1] += cell_size
        if direction == 2:
            new_piece[0] -= cell_size
        if direction == 3:
            new_piece[1] -= cell_size
        if direction == 4:
            new_piece[0] += cell_size

        #attach new segment
        snake_pos.append(new_piece)

        #increase score
        score += 1

    if update_snake > 99:
        update_snake = 0

        snake_pos = snake_pos[-1:] + snake_pos[:-1]
        # upward
        if direction == 1:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] - cell_size
        if direction == 2:
            snake_pos[0][1] = snake_pos[1][1]
            snake_pos[0][0] = snake_pos[1][0] + cell_size
        if direction == 3:
            snake_pos[0][0] = snake_pos[1][0]
            snake_pos[0][1] = snake_pos[1][1] + cell_size
        if direction == 4:
            snake_pos[0][1] = snake_pos[1][1]
            snake_pos[0][0] = snake_pos[1][0] - cell_size

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

    update_snake += 1

# end game
pygame.quit()
