import pygame

pygame.mixer.init()

spriteSheet = target = rightCannon = hand = None

assaultRifle = []
pistol = []
pierceGun = []
sword = []
coolSword = []
swordSlash = []
slashBullet = []
bullet = []
bossWeapon = []

# player image
playerIdleRight = []
playerIdleLeft = []
playerWalkingRight = []
playerWalkingLeft = []
playerDeath = []

# enemy image
meleeEnemyWalkingRight = []
meleeEnemyWalkingLeft = []

# ui images
hudBar = []  # health bars and stuff like it
hudAssets = []
uiAssets = []
buttons = []
fonts = []

# sound effects
arSound = []
pistolSound = []
backgroundSound = []
pierceSound = []
resourceSound = []
bossSound = []
ultSound = []

# size of player images
WIDTH = 34
HEIGHT = 48

# colors
purple = (98,  22, 107)
blueGray = (186, 200, 216)
white = (229, 229, 242)
bgWhite = (68, 68, 97)


# set up the images after pygame has been initialized
def init():
    global spriteSheet, bullet, target, rightCannon,\
        assaultRifle, hand, sword, coolSword, playerIdleRight, playerIdleLeft, arSound, hudAssets, \
        hudbar, pistol, uiAssets, backgroundSound, swordSlash, fonts, buttons, slashBullet, playerDeath, pierceGun, \
        pierceSound, resourceSound, meleeEnemyWalkingRight, meleeEnemyWalkingLeft, boss, bossWeapon, bossSound, ultSound

    # sprite sheets
    spriteSheet = pygame.image.load("res/SpriteSheet.png").convert_alpha()
    gunSheet = loadImage("res/gunSheet.png", purple)
    playerSheet = pygame.transform.scale(loadImage("res/oneHandSheet.png", blueGray), (144, 208))
    playerWalkingSheet = pygame.transform.scale(loadImage("res/playerWalkingSheet.png", blueGray), (212, 232))
    deathSheet = loadImage("res/deathSheet.png", blueGray)
    hudSheet = pygame.image.load("res/hudSheet.png").convert_alpha()
    uiSheet = pygame.image.load("res/itemShopSheet.png").convert_alpha()
    slashSheet = pygame.image.load("res/slash.png").convert_alpha()
    meleeEnemySheet = pygame.image.load("res/meleeEnemySheet.png").convert_alpha()

    bullet.append(pygame.image.load("res/bullet.png").subsurface((40, 46, 45, 34)))  # crop the sprite sheet
    bullet.append(pygame.transform.flip(bullet[0], True, False))  # flip the image
    bullet.append(pygame.image.load("res/enemyBullet.png").subsurface((40, 46, 45, 34)))
    bullet.append(pygame.transform.flip(bullet[2], True, False))
    bullet.append(pygame.transform.scale(pygame.image.load("res/pierceBullet.png"), (100, 100)))
    bullet.append(pygame.transform.flip(bullet[4], True, False))
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

    playerDeath.append(deathSheet.subsurface((0, 0, WIDTH, HEIGHT)))
    playerDeath.append(deathSheet.subsurface((WIDTH, 0, WIDTH, HEIGHT)))
    playerDeath.append(deathSheet.subsurface((2 * WIDTH, 0, WIDTH, HEIGHT)))
    playerDeath.append(deathSheet.subsurface((3 * WIDTH, 0, WIDTH, HEIGHT)))
    playerDeath.append(deathSheet.subsurface((4 * WIDTH, 0, WIDTH, HEIGHT)))
    playerDeath.append(deathSheet.subsurface((5 * WIDTH, 0, WIDTH, HEIGHT)))
    playerDeath.append(deathSheet.subsurface((6 * WIDTH, 0, WIDTH, HEIGHT)))
    playerDeath.append(deathSheet.subsurface((7 * WIDTH, 0, WIDTH, HEIGHT)))

    meleeEnemyWalkingRight.append(meleeEnemySheet.subsurface((0, 0, WIDTH, HEIGHT)))
    meleeEnemyWalkingRight.append(meleeEnemySheet.subsurface((WIDTH, 0, WIDTH, HEIGHT)))
    meleeEnemyWalkingRight.append(meleeEnemySheet.subsurface((2 * WIDTH, 0, WIDTH, HEIGHT)))
    meleeEnemyWalkingRight.append(meleeEnemySheet.subsurface((3 * WIDTH, 0, WIDTH, HEIGHT)))
    meleeEnemyWalkingRight.append(meleeEnemySheet.subsurface((4 * WIDTH, 0, WIDTH, HEIGHT)))
    meleeEnemyWalkingRight.append(meleeEnemySheet.subsurface((5 * WIDTH, 0, WIDTH, HEIGHT)))

    meleeEnemyWalkingLeft.append(pygame.transform.flip(meleeEnemyWalkingRight[0], True, False).convert_alpha())
    meleeEnemyWalkingLeft.append(pygame.transform.flip(meleeEnemyWalkingRight[1], True, False).convert_alpha())
    meleeEnemyWalkingLeft.append(pygame.transform.flip(meleeEnemyWalkingRight[2], True, False).convert_alpha())
    meleeEnemyWalkingLeft.append(pygame.transform.flip(meleeEnemyWalkingRight[3], True, False).convert_alpha())
    meleeEnemyWalkingLeft.append(pygame.transform.flip(meleeEnemyWalkingRight[4], True, False).convert_alpha())
    meleeEnemyWalkingLeft.append(pygame.transform.flip(meleeEnemyWalkingRight[5], True, False).convert_alpha())

    baseRifle = pygame.transform.scale(pygame.image.load("res/ar.png").subsurface((0, 0, 32, 32)), (64, 64))
    assaultRifle.append(baseRifle)
    assaultRifle.append(pygame.transform.flip(assaultRifle[0], True, False))

    basePierceGun = gunSheet.subsurface((0, 0, 96, 96))
    pierceGun.append(basePierceGun)
    pierceGun.append(pygame.transform.flip(pierceGun[0], True, False))

    baseSword = gunSheet.subsurface((96 * 3, 0, 96, 96))
    sword.append(baseSword)
    sword.append(pygame.transform.flip(sword[0], True, False))

    baseCoolSword = gunSheet.subsurface((96 * 4, 0, 96, 96))
    coolSword.append(baseCoolSword)
    coolSword.append(pygame.transform.flip(coolSword[0], True, False))

    swordSlash.append(slashSheet.subsurface((0, 0, 64, 64)))
    swordSlash.append(slashSheet.subsurface((64, 0, 64, 64)))
    swordSlash.append(slashSheet.subsurface((2 * 64, 0, 64, 64)))
    swordSlash.append(slashSheet.subsurface((3 * 64, 0, 64, 64)))
    swordSlash.append(slashSheet.subsurface((4 * 64, 0, 64, 64)))
    swordSlash.append(slashSheet.subsurface((0, 64, 64, 64)))
    swordSlash.append(slashSheet.subsurface((64, 64, 64, 64)))

    baseSB = pygame.image.load("res/slashProjectile.png")
    slashBullet.append(baseSB)
    slashBullet.append(pygame.transform.flip(slashBullet[0], True, False))

    basePistol = pygame.transform.scale(pygame.image.load("res/ar.png").subsurface((32, 0, 32, 32)), (64, 64))
    pistol.append(basePistol)
    pistol.append(pygame.transform.flip(pistol[0], True, False))

    bossWeaponBase = pygame.image.load("res/bossWeapon.png")
    bossWeapon.append(bossWeaponBase)
    bossWeapon.append(pygame.transform.flip(bossWeapon[0], True, False))


    hand = pygame.transform.scale(pygame.image.load("res/hand.png"), (8, 8))
    hand.set_colorkey((186, 200, 216))

    boss = pygame.image.load("res/boss.png")

    hudAssets.append(hudSheet.subsurface((0, 0, 84, 64)))
    hudAssets.append(hudSheet.subsurface((103, 0, 32, 64)))
    grayBar1 = hudSheet.subsurface((85, 4, 8, 15))
    grayBar2 = hudSheet.subsurface((94, 4, 8, 15))
    hudBar.append([grayBar1, grayBar2])
    redBar1 = hudSheet.subsurface((144, 4, 8, 15))
    redBar2 = hudSheet.subsurface((153, 4, 8, 15))
    hudBar.append([redBar1, redBar2])
    blueBar1 = hudSheet.subsurface((144, 24, 8, 15))
    blueBar2 = hudSheet.subsurface((153, 24, 8, 15))
    hudBar.append([blueBar1, blueBar2])
    greenBar1 = hudSheet.subsurface((144, 44, 8, 15))
    greenBar2 = hudSheet.subsurface((153, 44, 8, 15))
    hudBar.append([greenBar1, greenBar2])

    uiAssets.append(pygame.transform.scale(uiSheet.subsurface((0, 0, 32 * 11, 260)), (528, 390)))  # item shop
    uiAssets.append(pygame.transform.scale(uiSheet.subsurface((0, 32 * 9, 32 * 6, 40)), (288, 60)))  # item block
    uiAssets.append(
        pygame.transform.scale(uiSheet.subsurface((32 * 6, 32 * 9, 32 * 6, 40)), (288, 60)))  # light item block
    uiAssets.append(
        pygame.transform.scale(uiSheet.subsurface((32 * 15, 0, 32 * 5, 32 * 4)),
                               (32 * 5 * (3/2), 32 * 4 * (3/2))))  # small text box
    uiAssets.append(
        pygame.transform.scale(uiSheet.subsurface((32 * 15, 32 * 4, 32 * 6, 228)),
                               (32 * 6 * (3/2), 228 * (3/2))))  # main menu
    uiAssets.append(
        pygame.transform.scale(uiSheet.subsurface((32 * 14, 32 * 12, 32 * 6, 40)),
                               (32 * 6 * (3 / 2), 40 * (3 / 2))))  # menu text box
    uiAssets.append(
        pygame.transform.scale(uiSheet.subsurface((32 * 20, 32 * 12, 32 * 6, 40)),
                               (32 * 6 * (3 / 2), 40 * (3 / 2))))  # light menu text box
    uiAssets.append(
        pygame.transform.scale(uiSheet.subsurface((32 * 21, 32 * 1, 32 * 5, 32 * 4)),
                               (32 * 5 * (3 / 2), 32 * 4 * (3 / 2))))  # instruction box

    buttons.append(pygame.transform.scale(uiSheet.subsurface((32 * 20, 0, 32, 32)), (48, 48)))
    buttons.append(pygame.transform.scale(uiSheet.subsurface((32 * 21, 0, 32, 32)), (48, 48)))
    buttons.append(pygame.transform.scale(uiSheet.subsurface((32 * 22, 0, 32, 32)), (48, 48)))

    fonts.append(pygame.font.Font("res/slkscr.ttf", 16))
    fonts.append(pygame.font.Font("res/slkscr.ttf", 18))
    fonts.append(pygame.font.Font("res/slkscr.ttf", 36))

    arSound.append(pygame.mixer.Sound("res/sfx/arShot.wav"))
    arSound[0].set_volume(0.05)
    arSound.append(pygame.mixer.Sound("res/sfx/arReload.wav"))
    arSound[1].set_volume(0.05)

    pistolSound.append(pygame.mixer.Sound("res/sfx/pistolShot.wav"))
    pistolSound[0].set_volume(0.01)
    pistolSound.append(pygame.mixer.Sound("res/sfx/pistolReload.wav"))
    pistolSound[1].set_volume(0.05)

    pierceSound.append(pygame.mixer.Sound("res/sfx/pierceShot.wav"))
    pierceSound[0].set_volume(0.05)

    backgroundSound.append(pygame.mixer.Sound("res/sfx/bg.mp3"))
    backgroundSound[0].set_volume(0.02)
    backgroundSound.append(pygame.mixer.Sound("res/sfx/waveClear.wav"))

    bossSound.append(pygame.mixer.Sound("res/sfx/bossSpawn.wav"))

    resourceSound.append(pygame.mixer.Sound("res/sfx/cashSound.mp3"))
    resourceSound.append(pygame.mixer.Sound("res/sfx/healthSound.wav"))
    resourceSound[1].set_volume(0.1)
    resourceSound.append(pygame.mixer.Sound("res/sfx/arReload.wav"))

    ultSound.append(pygame.mixer.Sound("res/sfx/shockwave.wav"))
    ultSound.append(pygame.mixer.Sound("res/sfx/invisibility.wav"))


# rotate a square image
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    """code works for square shaped images"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


# load an image and make the selected color transparent
def loadImage(path, key):
    image = pygame.image.load(path).convert_alpha()
    image.set_colorkey(key)
    return image


# render a font with a darker color behind it
def renderFont(display, string, color, bg_color, center_x, center_y, font):
    msg = font.render(string, False, bg_color)
    msg_rect = msg.get_rect(center=(center_x, center_y + 3))
    drawText(display, string, bg_color, msg_rect, font)
    msg = font.render(string, False, color)
    msg_rect = msg.get_rect(center=(center_x, center_y))
    drawText(display, string, color, msg_rect, font)


# render a text within a rect
def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = 1

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

        # remove the text we just blit
        text = text[i:]

    return text
