import world
import pygame

from gfx import assets
from states.state import State


class GameState(State):
    def __init__(self, game):
        super().__init__(game)
        self.world = world.World(self, "hello")

    def tick(self):
        if self.game.inputManager.keys[pygame.K_TAB]:
            pass
        self.world.tick()

    def render(self, display):
        self.world.render(display)
