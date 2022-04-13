import pygame

spriteSheet = cannon = bullet = target = leftCannon\
    = rightCannon = font = playerSheet = sword = gunSheet = hand = None
assaultRifle = [None] * 12
WIDTH = 18
HEIGHT = 26

#colors
purple = ( 98,  22, 107)

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
    leftCannon = pygame.transform.flip(rightCannon, True, False)
    target = spriteSheet.subsurface((0, 0, 32, 32))

    sword = pygame.image.load("res/sword.png")

    baseRifle = pygame.transform.scale(gunSheet.subsurface((234, 18, 70, 70)), (45, 45))
    assaultRifle[3] = baseRifle
    assaultRifle[9] = pygame.transform.flip(baseRifle, True, False)

    hand = pygame.transform.scale(pygame.image.load("res/hand.png"), (8, 8))
    hand.set_colorkey((186, 200, 216))

    font = pygame.font.Font("res/slkscr.ttf", 36)
