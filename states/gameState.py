import world
import pygame

from states.state import State


class GameState(State):
    def __init__(self, game):
        super().__init__(game)
        self.world = world.World(self.game, "hello")

    def tick(self):
        if self.game.get_inputManager().get_keys()[pygame.K_TAB]:
            pass
        self.world.tick()

    def render(self, display):
        self.world.render(display)

    def get_game(self):
        return self.game
