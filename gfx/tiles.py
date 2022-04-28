import random

import pygame


class Tile:
    WIDTH = 32
    HEIGHT = 32
    floorSheet = pygame.image.load("res/floor.png")
    wallSheet = pygame.image.load("res/wall.png")
    def __init__(self, c):
        self.color = c
        self.image = None
        self.isSolid = False
        if c[1] == 0:
            self.image = pygame.surface.Surface((32, 32))
            self.image.fill((36, 43, 43))
        elif c[1] == 1:
            self.image = None
        elif c[1] == 50:  # bottom of wall
            self.image = Tile.wallSheet.subsurface((32 * 1, 32 * 3, 32, 32)).copy()
        elif c[1] == 150: # top of wall
            self.image = Tile.wallSheet.subsurface((32 * 1, 32 * 2, 32, 32)).copy()

        elif c[1] == 200: # first part of stair
            self.image = Tile.wallSheet.subsurface((32 * 5, 0, 32, 32)).copy()
        elif c[1] == 201: # second part of stair
            self.image = Tile.wallSheet.subsurface((32 * 6, 0, 32, 32)).copy()
        elif c[1] == 202: # third part of stair
            self.image = Tile.wallSheet.subsurface((32 * 5, 32, 32, 32)).copy()
        elif c[1] == 203: # fourth part of stair
            self.image = Tile.wallSheet.subsurface((32 * 6, 32, 32, 32)).copy()
        elif c[1] == 204: # fifth part of stair
            self.image = Tile.wallSheet.subsurface((32 * 5, 32 * 2, 32, 32)).copy()
        elif c[1] == 205: # sixth part of stair
            self.image = Tile.wallSheet.subsurface((32 * 6, 32 * 2, 32, 32)).copy()

        elif c[1] == 255:  # floor tile
            self.image = Tile.floorSheet.subsurface((0, 0, 32, 32)).copy()
        else:
            self.image = pygame.surface.Surface((32, 32))
            self.image.fill((36, 43, 43))

        # r value is what image is blit on top of the base image
        if c[0] == 10:
            self.image.blit(Tile.wallSheet.subsurface((0, 0, 32, 32)), (0, 0))
        elif c[0] == 40:
            self.image.blit(Tile.wallSheet.subsurface((32, 0, 32, 32)), (0, 0))
        elif c[0] == 60:
            self.image.blit(Tile.wallSheet.subsurface((32 * 2, 0, 32, 32)), (0, 0))
        elif c[0] == 120:
            self.image.blit(Tile.wallSheet.subsurface((0, 32, 32, 32)), (0, 0))
        elif c[0] == 140:
            self.image.blit(Tile.wallSheet.subsurface((32 * 2, 32, 32, 32)), (0, 0))
        elif c[0] == 160:
            self.image.blit(Tile.wallSheet.subsurface((32 * 3, 32, 32, 32)), (0, 0))
        elif c[0] == 180:
            self.image.blit(Tile.wallSheet.subsurface((32 * 4, 32, 32, 32)), (0, 0))
        elif c[0] == 200:
            self.image.blit(Tile.wallSheet.subsurface((0, 32 * 2, 32, 32)), (0, 0))
        elif c[0] == 220:
            self.image.blit(Tile.wallSheet.subsurface((32 * 2, 32 * 2, 32, 32)), (0, 0))
        elif c[0] == 240:
            self.image.blit(Tile.wallSheet.subsurface((0, 32 * 3, 32, 32)), (0, 0))
        elif c[0] == 255:
            self.image.blit(Tile.wallSheet.subsurface((32 * 2, 32 * 3, 32, 32)), (0, 0))

        if c[2] == 0:
            self.isSolid = False
        else:
            self.isSolid = True

