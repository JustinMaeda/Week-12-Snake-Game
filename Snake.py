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


