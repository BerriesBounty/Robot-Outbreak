import random

import pygame


class Tile:
    WIDTH = 32
    HEIGHT = 32
    grassSheet = pygame.image.load("res/grass.png")
    wallSheet = pygame.image.load("res/wall.png")
    def __init__(self, c):
        self.color = c
        self.image = None
        self.isSolid = False
        if c[1] == 0:
            self.image = pygame.surface.Surface((32, 32))
            self.image.fill((119, 166, 115))
        elif c[1] == 50:
            self.image = Tile.wallSheet.subsurface((32 * 1, 32 * 3, 32, 32)).copy()
        elif c[1] == 150:
            self.image = Tile.wallSheet.subsurface((32 * 1, 32 * 2, 32, 32)).copy()
        elif c[1] == 255:
            num = random.randint(0, 100)
            if num < 50:
                x = 0
                y = 0
            else:
                x = 32 * random.randint(1, 5)
                y = 32 * random.randint(0, 3)
            self.image = Tile.grassSheet.subsurface((x, y, 32, 32)).copy()
        else:
            self.image = pygame.surface.Surface((32, 32))
            self.image.fill((119, 166, 115))

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

