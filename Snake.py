#import modules
import pygame
from pygame.locals import *

pygame.init()

#create blank game window
screen_width = 600
screen_height = 600

#create game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake')

#define background colors
bg = (255, 200, 150)

def draw_screen():
    screen.fill(bg)

#setup loop with exit
run = True
while run:

    #iterate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #update display
    pygame.display.update()


#end game
pygame.quit()