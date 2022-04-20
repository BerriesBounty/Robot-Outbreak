import pygame


class InputManager:
    def __init__(self, game):
        self.game = game
        self.keys = pygame.key.get_pressed()
        self.keyReleased = {}
        self.keyJustPressed = {}  # what key is JUST PRESSED

        self.mouse = [False, False]  # what mouse is pressed
        self.justPressed = [False, False]
        self.x = 0  # x and y position of the mouse
        self.y = 0
        self.offsetX = 0  # x and y position of the mouse relative to where the camera moved to
        self.offsetY = 0

    def tick(self):
        self.keys = pygame.key.get_pressed()  # get what key is held down
        for i in self.keyReleased:
            self.keyReleased[i] = False
        for i in self.keyJustPressed:
            self.keyJustPressed[i] = False
        self.justPressed = [False, False]  # set what keys and mouse is pressed this tick to false

        mouse = pygame.mouse.get_pos()  # position of mouse
        self.x = mouse[0]
        self.y = mouse[1]
        self.offsetX = mouse[0] + self.game.gameCamera.xOffset  # the mouse moves in the same direction as the camera
        self.offsetY = mouse[1] + self.game.gameCamera.yOffset

    def keyUp(self, event):  # when a key is released
        if event.key == pygame.K_SPACE:
            self.keyReleased["space"] = True  #set the keyReleased to true just for this tick

    def keyDown(self, event):  # when a key is pressed down
        if event.key == pygame.K_SPACE:
            self.keyJustPressed["space"] = True
        if event.key == pygame.K_r:
            self.keyJustPressed["r"] = True
        if event.key == pygame.K_TAB:
            self.keyJustPressed["tab"] = True
        if event.key == pygame.K_q:
            self.keyJustPressed["q"] = True
        if event.key == pygame.K_UP:
            self.keyJustPressed["up"] = True
        if event.key == pygame.K_DOWN:
            self.keyJustPressed["down"] = True

    def mousePressed(self):  # when a mouse is pressed
        if pygame.mouse.get_pressed()[0]:
            self.mouse[0] = True
            self.justPressed[0] = True
        elif pygame.mouse.get_pressed()[1]:
            self.mouse[1] = True
            self.justPressed[1] = True

    def mouseReleased(self):  # when a mouse is released
        if not pygame.mouse.get_pressed()[0]:
            self.mouse[0] = False
        elif not pygame.mouse.get_pressed()[1]:
            self.mouse[1] = False

    def get_pressed(self, n):  # return if a mouse button is prssed down
        return self.mouse[n]
