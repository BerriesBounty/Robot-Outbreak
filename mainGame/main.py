import pygame, sys
from pygame.locals import *  # imports functions
import cannon, game
pygame.init()  # initialize modules

game = cannon.Game("BOB", 800, 600)
game.start()
