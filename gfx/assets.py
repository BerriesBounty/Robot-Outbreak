import pygame

pygame.mixer.init()

spriteSheet = cannon = bullet = target = leftCannon\
    = rightCannon = font36 = font18 = hand = None

assaultRifle = []
pistol = []
sword = []
swordSlash = []

playerIdleRight = []
playerIdleLeft = []
playerWalkingRight = []
playerWalkingLeft = []

hudbar = []
hudAssets = []
uiAssets = []
buttons = []
fonts = []

arSound = []
pistolSound = []
backgroundSound = []

WIDTH = 34
HEIGHT = 48

#colors
purple = (98,  22, 107)

def init():
    global spriteSheet, bullet, cannon, target, leftCannon, rightCannon,\
        assaultRifle, hand, sword, playerIdleRight, playerIdleLeft, arSound, hudAssets, \
        hudbar, pistol, uiAssets, backgroundSound, swordSlash, fonts, buttons

    #sprite sheets
    spriteSheet = pygame.image.load("res/SpriteSheet.png").convert_alpha()
    gunSheet = loadImage("res/gunSheet.png", purple)
    playerSheet = pygame.transform.scale(loadImage("res/oneHandSheet.png", (186, 20, 216)), (144, 208))
    playerWalkingSheet = pygame.transform.scale(loadImage("res/playerWalkingSheet.png", (186, 20, 216)), (212, 232))
    hudSheet = pygame.image.load("res/hudSheet.png").convert_alpha()
    uiSheet = pygame.image.load("res/itemShopSheet.png").convert_alpha()
    slashSheet = pygame.image.load("res/slash.png").convert_alpha()

    bullet = spriteSheet.subsurface((16, 32, 16, 16))
    target = spriteSheet.subsurface((0, 0, 32, 32))

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

    baseRifle = pygame.transform.scale(pygame.image.load("res/ar.png").subsurface((0,0,32,32)), (64, 64))
    assaultRifle.append(baseRifle)
    assaultRifle.append(pygame.transform.flip(assaultRifle[0], True, False))

    baseSword = gunSheet.subsurface((96 * 3, 0, 96, 96))
    sword.append(baseSword)
    sword.append(pygame.transform.flip(sword[0], True, False))

    swordSlash.append(slashSheet.subsurface((0, 0, 64, 64)))
    swordSlash.append(slashSheet.subsurface((64, 0, 64, 64)))
    swordSlash.append(slashSheet.subsurface((2 * 64, 0, 64, 64)))
    swordSlash.append(slashSheet.subsurface((3 * 64, 0, 64, 64)))
    swordSlash.append(slashSheet.subsurface((4 * 64, 0, 64, 64)))
    swordSlash.append(slashSheet.subsurface((0, 64, 64, 64)))
    swordSlash.append(slashSheet.subsurface((64, 64, 64, 64)))

    basePistol = pygame.transform.scale(pygame.image.load("res/ar.png").subsurface((32,0,32,32)), (64, 64))
    pistol.append(basePistol)
    pistol.append(pygame.transform.flip(pistol[0], True, False))

    hand = pygame.transform.scale(pygame.image.load("res/hand.png"), (8, 8))
    hand.set_colorkey((186, 200, 216))

    hudAssets.append(hudSheet.subsurface((0, 0, 84, 64)))
    hudAssets.append(hudSheet.subsurface((103, 0, 32, 64)))
    graybar1 = hudSheet.subsurface((85, 4, 8, 15))
    graybar2 = hudSheet.subsurface((94, 4, 8, 15))
    hudbar.append([graybar1, graybar2])
    redbar1 = hudSheet.subsurface((144, 4, 8, 15))
    redbar2 = hudSheet.subsurface((153, 4, 8, 15))
    hudbar.append([redbar1, redbar2])
    bluebar1 = hudSheet.subsurface((144, 24, 8, 15))
    bluebar2 = hudSheet.subsurface((153, 24, 8, 15))
    hudbar.append([bluebar1, bluebar2])
    greenbar1 = hudSheet.subsurface((144, 44, 8, 15))
    greenbar2 = hudSheet.subsurface((153, 44, 8, 15))
    hudbar.append([greenbar1, greenbar2])

    uiAssets.append(pygame.transform.scale(uiSheet.subsurface((0, 0, 32 * 11, 260)), (528, 390)))
    uiAssets.append(pygame.transform.scale(uiSheet.subsurface((0, 32 * 9, 32 * 6, 40)), (288, 60)))
    uiAssets.append(pygame.transform.scale(uiSheet.subsurface((32 * 6, 32 * 9, 32 * 6, 40)), (288, 60)))
    uiAssets.append(pygame.transform.scale(uiSheet.subsurface((32 * 15, 0, 32 * 5, 32 * 4)), (32 * 5 * (3/2), 32 * 4 * (3/2))))
    uiAssets.append(pygame.transform.scale(uiSheet.subsurface((32 * 15, 32 * 3, 32 * 6, 106)), (32 * 6 * (3/2), 106 * (3/2))))

    buttons.append(pygame.transform.scale(uiSheet.subsurface((32 * 20, 0, 32, 32)), (48, 48)))
    buttons.append(pygame.transform.scale(uiSheet.subsurface((32 * 21, 0, 32, 32)), (48, 48)))
    buttons.append(pygame.transform.scale(uiSheet.subsurface((32 * 22, 0, 32, 32)), (48, 48)))

    fonts.append(pygame.font.Font("res/slkscr.ttf", 16))
    fonts.append(pygame.font.Font("res/slkscr.ttf", 18))
    fonts.append(pygame.font.Font("res/slkscr.ttf", 36))

    arSound.append(pygame.mixer.Sound("res/sfx/arShot.wav"))
    arSound[0].set_volume(0.01)
    arSound.append(pygame.mixer.Sound("res/sfx/arReload.wav"))
    arSound[1].set_volume(0.05)

    pistolSound.append(pygame.mixer.Sound("res/sfx/pistolShot.wav"))
    pistolSound[0].set_volume(0.01)
    pistolSound.append(pygame.mixer.Sound("res/sfx/pistolReload.wav"))
    pistolSound[1].set_volume(0.05)

    backgroundSound.append(pygame.mixer.Sound("res/sfx/background.mp3"))
    backgroundSound[0].set_volume(0.5)


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
    image = pygame.image.load(path).convert_alpha()
    image.set_colorkey(key)
    return image

def renderFont(display, string, color, bgcolor, centerX, centerY, font):
    msg = font.render(string, False, bgcolor)
    msg_rect = msg.get_rect(center=(centerX, centerY + 3))
    drawText(display, string, bgcolor, msg_rect, font)
    msg = font.render(string, False, color)
    msg_rect = msg.get_rect(center=(centerX, centerY))
    # display.blit(msg, msg_rect)
    drawText(display, string, color, msg_rect, font)

def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text
