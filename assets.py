import pygame

spriteSheet = cannon = bullet = target = leftCannon\
    = rightCannon = font = playerSheet = sword = gunSheet = hand = None
assaultRifle = [None] * 2
WIDTH = 18
HEIGHT = 26

#colors
purple = ( 98,  22, 107)

def init():
    global spriteSheet, bullet, cannon, target, leftCannon, rightCannon, font, \
        playerSheet, sword, gunSheet, assaultRifle, hand
    spriteSheet = pygame.image.load("res/SpriteSheet.png").convert_alpha()
    gunSheet = loadImage("res/gunSheet.png", purple)
    playerSheet = loadImage("res/oneHandSheet.png", (186, 200, 216))

    bullet = spriteSheet.subsurface((16, 32, 16, 16))
    cannon = playerSheet.subsurface((0, 0, WIDTH, HEIGHT))
    rightCannon = playerSheet.subsurface((0, HEIGHT, WIDTH, HEIGHT))
    leftCannon = pygame.transform.flip(rightCannon, True, False)
    target = spriteSheet.subsurface((0, 0, 32, 32))

    sword = pygame.image.load("res/sword.png")

    baseRifle = pygame.transform.scale(gunSheet.subsurface((0, 0, 96, 96)), (48, 48))
    assaultRifle[0] = baseRifle
    assaultRifle[1] = pygame.transform.flip(baseRifle, True, False)

    hand = pygame.transform.scale(pygame.image.load("res/hand.png"), (8, 8))
    hand.set_colorkey((186, 200, 216))

    font = pygame.font.Font("res/slkscr.ttf", 36)

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
