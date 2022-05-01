import pygame
import sys
import time
from pygame.locals import *  # imports functions
from gfx import assets
import inputManager as inputManager
import states.gameState as gameState
import states.state
from gfx.gameCamera import GameCamera
from states import startingState


class Game:
    def __init__(self, name, width, height):
        pygame.init()  # initialize modules
        self.name = name  # name of program
        self.width = width  # width/height of program
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))

        self.inputManager = inputManager.InputManager(self)  # taking in all inputs of keyboard & mouse
        self.gameCamera = GameCamera(self, 0, 0)  # manage what the screen can see
        self.clock = pygame.time.Clock()
        assets.init()  # assets class stores all the images

        # states are the different parts of a game
        self.stateManager = states.state.StateManager()
        self.gameState = gameState.GameState(self)  # the actual gameplay
        self.startingState = startingState.StartingState(self)  # the stating menu
        self.stateManager.set_state(self.startingState)  # set the current state the game is in
        self.background = pygame.transform.scale(pygame.image.load("res/menuBg.jpg"),
                                                 (800, 600))  # the background image
        assets.backgroundSound[0].play()

    def start(self):  # the main while loop of the game

        fps = 30  # how many ticks per second
        timesPerTick = 1000000000 / fps  # number of nanosecond between each tick
        delta = 0
        lastTime = time.perf_counter_ns()  # the last time it ticked
        timer = 0
        ticks = 0

        while True:

            now = time.perf_counter_ns()  # time of the current loop
            delta += (now - lastTime) / timesPerTick  # how many ticks can be performed in the
            timer += now - lastTime  # amount of time past
            lastTime = now

            if delta >= 1:
                self.tick()
                self.render(self.display)
                ticks += 1
                delta -= 1

            if timer >= 1000000000:  # if it has been a second
                print(f"fps: {ticks}")
                ticks = 0
                timer = 0

            # self.tick()  # updating on the different classes
            # self.render(self.display)  # drawing all the sprites

            pygame.display.update()
            # self.clock.tick(30)

    def tick(self):  # basically update
        self.inputManager.tick()  # manage what key and mouse button is hold down and the position of mouse
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # if a key is pressed down
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                self.inputManager.keyDown(event)  # let the inputManager to store what key is pressed
            if event.type == pygame.KEYUP:  # if a key is released
                self.inputManager.keyUp(event)
            if event.type == pygame.MOUSEBUTTONDOWN:  # if a mouse button is pressed down
                self.inputManager.mousePressed()
            if event.type == pygame.MOUSEBUTTONUP:
                self.inputManager.mouseReleased()  # if a mouse button is released

        pygame.display.set_caption(f"X: {self.inputManager.x} Y: {self.inputManager.y}")  # show the mouse position

        if self.stateManager.get_state() is not None:  # if there is a current state
            self.stateManager.get_state().tick()  # update the state

    def render(self, display):  # draws what is on screen every loop. Display is the screen to blit on
        display.fill((0, 0, 0))  # clear the display
        display.blit(self.background, (0, 0))  # display background image
        if self.stateManager.get_state() is not None:  # make sure no error will happen
            self.stateManager.get_state().render(display)  # render the state
