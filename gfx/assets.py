import pygame

spriteSheet = cannon = bullet = target = leftCannon\
    = rightCannon = font36 = playerSheet = gunSheet = hand = None

assaultRifle = []
sword = []

playerIdleRight = []
playerIdleLeft = []

WIDTH = 36
HEIGHT = 48

#colors
purple = (98,  22, 17)

def init():
    global spriteSheet, bullet, cannon, target, leftCannon, rightCannon, font36, \
        playerSheet, gunSheet, assaultRifle, hand, sword, playerIdleRight, playerIdleLeft
    spriteSheet = pygame.image.load("res/SpriteSheet.png").convert_alpha()
    gunSheet = loadImage("res/gunSheet.png", purple)
    playerSheet = pygame.transform.scale(loadImage("res/oneHandSheet.png", (186, 200, 216)), (144, 208))

    bullet = spriteSheet.subsurface((16, 32, 16, 16))
    target = spriteSheet.subsurface((0, 0, 32, 32))

    cannon = playerSheet.subsurface((0, 0, WIDTH, HEIGHT))
    rightCannon = playerSheet.subsurface((0, HEIGHT, WIDTH, HEIGHT))
    leftCannon = pygame.transform.flip(rightCannon, True, False)

    playerIdleRight.append(playerSheet.subsurface((0, HEIGHT, WIDTH, HEIGHT)))
    playerIdleRight.append(playerSheet.subsurface((WIDTH, HEIGHT, WIDTH, HEIGHT)))
    playerIdleRight.append(playerSheet.subsurface((2 * WIDTH, HEIGHT, WIDTH, HEIGHT)))
    playerIdleRight.append(playerSheet.subsurface((3 * WIDTH, HEIGHT, WIDTH, HEIGHT)))

    playerIdleLeft.append(pygame.transform.flip(playerIdleRight[0], True, False))
    playerIdleLeft.append(pygame.transform.flip(playerIdleRight[1], True, False))
    playerIdleLeft.append(pygame.transform.flip(playerIdleRight[2], True, False))
    playerIdleLeft.append(pygame.transform.flip(playerIdleRight[3], True, False))

    baseRifle = pygame.transform.scale(gunSheet.subsurface((0, 0, 96, 96)), (48, 48))
    assaultRifle.append(baseRifle)
    assaultRifle.append(pygame.transform.flip(assaultRifle[0], True, False))

    baseSword = gunSheet.subsurface((96 * 3, 0, 96, 96))
    sword.append(baseSword)
    sword.append(pygame.transform.flip(sword[0], True, False))


    hand = pygame.transform.scale(pygame.image.load("res/hand.png"), (8, 8))
    hand.set_colorkey((186, 200, 216))

    font36 = pygame.font.Font("res/slkscr.ttf", 36)

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    """code works for square shaped images"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def loadImage(path, key):
    image = pygame.image.load(path)
    image.set_colorkey(key)
    return image
