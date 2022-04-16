import pygame

spriteSheet = cannon = bullet = target = leftCannon\
    = rightCannon = font36 = hand = playerIcon = None

assaultRifle = []
sword = []

playerIdleRight = []
playerIdleLeft = []
playerWalkingRight = []
playerWalkingLeft = []

hudbar = []

arSound = []

WIDTH = 34
HEIGHT = 48

#colors
purple = (98,  22, 107)

def init():
    global spriteSheet, bullet, cannon, target, leftCannon, rightCannon, font36,\
        assaultRifle, hand, sword, playerIdleRight, playerIdleLeft, arSound, playerIcon, hudbar

    #sprite sheets
    spriteSheet = pygame.image.load("res/SpriteSheet.png").convert_alpha()
    gunSheet = loadImage("res/gunSheet.png", purple)
    playerSheet = pygame.transform.scale(loadImage("res/oneHandSheet.png", (186, 200, 216)), (144, 208))
    playerWalkingSheet = pygame.transform.scale(loadImage("res/playerWalkingSheet.png", (186, 200, 216)), (212, 232))
    hudSheet = pygame.image.load("res/hudSheet.png").convert_alpha()

    bullet = spriteSheet.subsurface((16, 32, 16, 16))
    target = spriteSheet.subsurface((0, 0, 32, 32))

    cannon = playerSheet.subsurface((0, 0, WIDTH, HEIGHT))
    rightCannon = playerSheet.subsurface((0, HEIGHT, WIDTH, HEIGHT))
    leftCannon = pygame.transform.flip(rightCannon, True, False)

    playerIdleRight.append(playerSheet.subsurface((0, HEIGHT, WIDTH, HEIGHT)))
    playerIdleRight.append(playerSheet.subsurface((WIDTH, HEIGHT, WIDTH, HEIGHT)))
    playerIdleRight.append(playerSheet.subsurface((2 * WIDTH, HEIGHT, WIDTH, HEIGHT)))
    playerIdleRight.append(playerSheet.subsurface((3 * WIDTH, HEIGHT, WIDTH, HEIGHT)))

    playerIdleLeft.append(pygame.transform.flip(playerIdleRight[0], True, False).convert_alpha())
    playerIdleLeft.append(pygame.transform.flip(playerIdleRight[1], True, False).convert_alpha())
    playerIdleLeft.append(pygame.transform.flip(playerIdleRight[2], True, False).convert_alpha())
    playerIdleLeft.append(pygame.transform.flip(playerIdleRight[3], True, False).convert_alpha())

    playerWalkingRight.append(playerWalkingSheet.subsurface((0, HEIGHT, WIDTH, HEIGHT)))
    playerWalkingRight.append(playerWalkingSheet.subsurface((WIDTH, HEIGHT, WIDTH, HEIGHT)))
    playerWalkingRight.append(playerWalkingSheet.subsurface((WIDTH * 2, HEIGHT, WIDTH, HEIGHT)))
    playerWalkingRight.append(playerWalkingSheet.subsurface((WIDTH * 3, HEIGHT, WIDTH, HEIGHT)))
    playerWalkingRight.append(playerWalkingSheet.subsurface((WIDTH * 4, HEIGHT, WIDTH, HEIGHT)))
    playerWalkingRight.append(playerWalkingSheet.subsurface((WIDTH * 5, HEIGHT, WIDTH, HEIGHT)))

    playerWalkingLeft.append(pygame.transform.flip(playerWalkingRight[0], True, False).convert_alpha())
    playerWalkingLeft.append(pygame.transform.flip(playerWalkingRight[1], True, False).convert_alpha())
    playerWalkingLeft.append(pygame.transform.flip(playerWalkingRight[2], True, False).convert_alpha())
    playerWalkingLeft.append(pygame.transform.flip(playerWalkingRight[3], True, False).convert_alpha())
    playerWalkingLeft.append(pygame.transform.flip(playerWalkingRight[4], True, False).convert_alpha())
    playerWalkingLeft.append(pygame.transform.flip(playerWalkingRight[5], True, False).convert_alpha())

    baseRifle = pygame.transform.scale(gunSheet.subsurface((0, 0, 96, 96)), (48, 48))
    assaultRifle.append(baseRifle)
    assaultRifle.append(pygame.transform.flip(assaultRifle[0], True, False))

    baseSword = gunSheet.subsurface((96 * 3, 0, 96, 96))
    sword.append(baseSword)
    sword.append(pygame.transform.flip(sword[0], True, False))

    hand = pygame.transform.scale(pygame.image.load("res/hand.png"), (8, 8))
    hand.set_colorkey((186, 200, 216))

    playerIcon = hudSheet.subsurface((0, 0, 84, 64))
    graybar1 = hudSheet.subsurface((85, 5, 8, 15))
    graybar2 = hudSheet.subsurface((94, 5, 8, 15))
    hudbar.append([graybar1, graybar2])
    redbar1 = hudSheet.subsurface((144, 5, 8, 15))
    redbar2 = hudSheet.subsurface((153, 5, 8, 15))
    hudbar.append([redbar1, redbar2])

    font36 = pygame.font.Font("res/slkscr.ttf", 36)

    arSound.append(pygame.mixer.Sound("res/sfx/arShot.wav"))
    arSound[0].set_volume(0.05)
    arSound.append(pygame.mixer.Sound("res/sfx/arReload.wav"))


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
