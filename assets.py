import pygame

spriteSheet = cannon = bullet = target = leftCannon\
    = rightCannon = font = playerSheet = sword = None
WIDTH = 18
HEIGHT = 26


def init():
    global spriteSheet, bullet, cannon, target, leftCannon, rightCannon, font, playerSheet, sword
    spriteSheet = pygame.image.load("res/SpriteSheet.png").convert_alpha()
    playerSheet = pygame.image.load("res/playerSpriteSheet.png")
    playerSheet.set_colorkey((186, 200, 216))

    bullet = spriteSheet.subsurface((16, 32, 16, 16))
    cannon = playerSheet.subsurface((0, 0, WIDTH, HEIGHT))
    rightCannon = playerSheet.subsurface((0, HEIGHT, WIDTH, HEIGHT))
    leftCannon = pygame.transform.flip(rightCannon, WIDTH, 0)

    sword = pygame.image.load("res/sword.png")
    target = spriteSheet.subsurface((0, 0, 32, 32))
    font = pygame.font.Font("res/slkscr.ttf", 36)