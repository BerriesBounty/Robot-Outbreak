import pygame.font

from gfx import assets
from states.state import State


class StartingState(State):
    def __init__(self, game):
        super().__init__(game)
        self.curStage = 0

    def tick(self):
        pass
        if self.curStage == 0:
            if self.game.inputManager.keyReleased.get("space"):
                self.curStage = 1
                self.game.stateManager.set_state(self.game.gameState)

    def render(self, display):
        display.fill((0, 0, 0))
        if self.curStage == 0:
            assets.renderFont(display, "PRESS SPACE TO START", (229, 229, 242), (68, 68, 97), self.game.width / 2,
                        self.game.height / 2, assets.font36)
