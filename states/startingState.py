import pygame.font

from gfx import assets
from states.state import State


class StartingState(State):
    def __init__(self, game):
        super().__init__(game)

    def tick(self):
        pass
        if self.game.get_inputManager().get_keyReleased()[pygame.K_SPACE]:
            self.game.get_stateManager().set_state(self.game.gameState)

    def render(self, display):
        display.fill((0, 0, 0))
        msg = assets.font.render("PRESS SPACE TO START", False, (255, 255, 255))
        msg_rect = msg.get_rect(center=(self.game.get_width()/2, self.game.get_height()/2))
        display.blit(msg, msg_rect)
