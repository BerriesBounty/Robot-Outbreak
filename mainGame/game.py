import pygame
import sys
import time
from pygame.locals import *  # imports functions
import assets
import input.inputManager as inputManager
import states.gameState as gameState
import states.state
from states import startingState


class Game:
    def __init__(self, name, width, height):
        pygame.init()  # initialize modules
        self.name = name
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height))
        self.inputManager = inputManager.InputManager()
        self.clock = pygame.time.Clock()
        assets.init()

        self.stateManager = states.state.StateManager()
        self.gameState = gameState.GameState(self)
        self.startingState = startingState.StartingState(self)
        self.stateManager.set_state(self.startingState)

    def start(self):

        fps = 60  # how many ticks per second
        timesPerTick = 1000000000 / fps  # number of nanosecond between each tick
        delta = 0
        now = None
        lastTime = time.perf_counter_ns()  # the last time it ticked
        timer = 0
        ticks = 0

        while True:

            # now = time.perf_counter_ns() #time of the current loop
            # delta += (now - lastTime) / timesPerTick #how many ticks can be performed in the
            # timer += now - lastTime #amount of time past
            # lastTime = now
            #
            # if delta >= 1:
            #     self.tick()
            #     self.render()
            #     ticks += 1
            #     delta -= 1
            #
            # if timer >= 1000000000:#if it has been a second
            #     print(f"fps: {ticks}")
            #     ticks = 0
            #     timer = 0
            self.tick()
            self.render(self.display)

            pygame.display.update()
            self.clock.tick(60)

    def tick(self):
        self.inputManager.tick()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # if a key is pressed down
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYUP:
                self.inputManager.keyUp(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.inputManager.mousePressed()
            if event.type == pygame.MOUSEBUTTONUP:
                self.inputManager.mouseReleased()
            if event.type == pygame.MOUSEMOTION:
                self.inputManager.mouseMoved()

        pygame.display.set_caption(f"X: {self.inputManager.get_x()} Y: {self.inputManager.get_y()}")

        if self.stateManager.get_state() is not None:
            self.stateManager.get_state().tick()

    def render(self, display):
        display.fill((100, 100, 100))

        if self.stateManager.get_state() is not None:
            self.stateManager.get_state().render(display)

    def get_inputManager(self):
        return self.inputManager

    def get_stateManager(self):
        return self.stateManager

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
