import world
import pygame

from gfx import assets
from states.state import State
from ultimates.ult_invisible import Invisible


class GameState(State):
    def __init__(self, game):
        super().__init__(game)
        self.ultimateList = []
        self.ultimateList.append(Invisible(self, 5, 100))
        self.world = world.World(self, "hello")


    def tick(self):
        self.world.tick()

    def render(self, display):
        self.world.render(display)
