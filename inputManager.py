import pygame


class InputManager:
    def __init__(self, game):
        self.game = game
        self.keys = pygame.key.get_pressed()
        self.keyReleased = [False] * len(self.keys)
        self.mouse = [False, False]
        self.cantPress = [False, False]
        self.justPressed = [False, False]
        self.x = 0
        self.y = 0
        self.offsetX = 0
        self.offsetY = 0

    def tick(self):
        for i in range(len(self.mouse)):
            if self.cantPress[i] and not self.mouse[i]:
                self.cantPress[i] = False
            elif self.justPressed[i]:
                self.cantPress[i] = True
                self.justPressed[i] = False
            if (not self.cantPress[i]) and self.mouse[i]:
                self.justPressed[i] = True
        self.keys = pygame.key.get_pressed()
        self.keyReleased = [False] * len(self.keys)

        mouse = pygame.mouse.get_pos()
        self.x = mouse[0]
        self.y = mouse[1]
        self.offsetX = mouse[0] + self.game.gameCamera.xOffset
        self.offsetY = mouse[1] + self.game.gameCamera.yOffset

    def keyUp(self, event):
        if event.key == pygame.K_SPACE:
            self.keyReleased[pygame.K_SPACE] = True

    def mousePressed(self):
        if pygame.mouse.get_pressed()[0]:
            self.mouse[0] = True
        elif pygame.mouse.get_pressed()[1]:
            self.mouse[1] = True

    def mouseReleased(self):
        if not pygame.mouse.get_pressed()[0]:
            self.mouse[0] = False
        elif not pygame.mouse.get_pressed()[1]:
            self.mouse[1] = False

    def get_pressed(self, n):
        return self.mouse[n]

    def get_justPressed(self, n):
        return self.justPressed[n]

