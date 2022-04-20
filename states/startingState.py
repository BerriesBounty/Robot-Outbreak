import pygame.font

from gfx import assets
from states.state import State


class StartingState(State):
    def __init__(self, game):
        super().__init__(game)

    def tick(self):
        pass
        if self.game.get_inputManager().get_keyReleased()["space"]:
            self.game.get_stateManager().set_state(self.game.gameState)

    def render(self, display):
        display.fill((0, 0, 0))
        assets.renderFont(display, "PRESS SPACE TO START", (229, 229, 242), (68, 68, 97), self.world.state.game.width / 2,
                          self.world.state.game.height / 2)
