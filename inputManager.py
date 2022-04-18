import pygame


class InputManager:
    def __init__(self, game):
        self.game = game
        self.keys = pygame.key.get_pressed()
        self.keyReleased = [False] * len(self.keys)
        self.keyJustPressed = [False] * len(self.keys)

        self.mouse = [False, False]
        self.cantPress = [False, False]
        self.justPressed = [False, False]
        self.x = 0
        self.y = 0
        self.offsetX = 0
        self.offsetY = 0

    def tick(self):
        self.justPressed = [False, False]
        self.keys = pygame.key.get_pressed()
        self.keyReleased = [False] * len(self.keys)
        self.keyJustPressed = [False] * len(self.keys)

        mouse = pygame.mouse.get_pos()
        self.x = mouse[0]
        self.y = mouse[1]
        self.offsetX = mouse[0] + self.game.gameCamera.xOffset
        self.offsetY = mouse[1] + self.game.gameCamera.yOffset

    def keyUp(self, event):
        if event.key == pygame.K_SPACE:
            self.keyReleased[pygame.K_SPACE] = True

    def keyDown(self, event):
        if event.key == pygame.K_SPACE:
            self.keyJustPressed[pygame.K_SPACE] = True
        if event.key == pygame.K_r:
            self.keyJustPressed[pygame.K_r] = True
        if event.key == pygame.K_TAB:
            self.keyJustPressed[pygame.K_TAB] = True
        if event.key == pygame.K_q:
            self.keyJustPressed[pygame.K_q] = True

    def mousePressed(self):
        if pygame.mouse.get_pressed()[0]:
            self.mouse[0] = True
            self.justPressed[0] = True
        elif pygame.mouse.get_pressed()[1]:
            self.mouse[1] = True
            self.justPressed[1] = True

    def mouseReleased(self):
        if not pygame.mouse.get_pressed()[0]:
            self.mouse[0] = False
        elif not pygame.mouse.get_pressed()[1]:
            self.mouse[1] = False

    def get_pressed(self, n):
        return self.mouse[n]
