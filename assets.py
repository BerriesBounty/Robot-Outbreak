import pygame

spriteSheet = cannon = bullet = target = leftCannon\
    = rightCannon = font = playerSheet = sword = gunSheet = assaultRifle = hand = None
WIDTH = 18
HEIGHT = 26


def init():
    global spriteSheet, bullet, cannon, target, leftCannon, rightCannon, font, \
        playerSheet, sword, gunSheet, assaultRifle, hand
    spriteSheet = pygame.image.load("res/SpriteSheet.png").convert_alpha()
    gunSheet = pygame.image.load("res/guns.png")
    gunSheet.set_colorkey((98, 22, 107))
    playerSheet = pygame.image.load("res/oneHandSheet.png")
    playerSheet.set_colorkey((186, 200, 216))

    bullet = spriteSheet.subsurface((16, 32, 16, 16))
    cannon = playerSheet.subsurface((0, 0, WIDTH, HEIGHT))
    rightCannon = playerSheet.subsurface((0, HEIGHT, WIDTH, HEIGHT))
    leftCannon = pygame.transform.flip(rightCannon, WIDTH, 0)

    sword = pygame.image.load("res/sword.png")
    assaultRifle = gunSheet.subsurface((234, 40, 70, 26))
    target = spriteSheet.subsurface((0, 0, 32, 32))

    hand = pygame.transform.scale(pygame.image.load("res/hand.png"), (8,8))
    hand.set_colorkey((186, 200, 216))

    font = pygame.font.Font("res/slkscr.ttf", 36)
