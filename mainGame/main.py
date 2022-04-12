import pygame, sys
from pygame.locals import *  # imports functions
import game
pygame.init()  # initialize modules

game = game.Game("BOB", 800, 600)
game.start()
