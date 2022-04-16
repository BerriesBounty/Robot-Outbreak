import math

from gfx import assets


class HUDManager():
    def __init__(self, world):
        self.world = world
        self.player = self.world.player
        self.healthBar = math.ceil(self.player.health / 10)

    def tick(self):
        self.healthBar = math.ceil(self.player.health / 10)

    def render(self, display):
        display.blit(assets.playerIcon, (10, 10))

        display.blit(assets.hudbar[0][0], (assets.playerIcon.get_width() + 10, 15))
        for i in range(1, 10):
            display.blit(assets.hudbar[0][1],
                         (assets.playerIcon.get_width() + 10 + assets.hudbar[0][1].get_width() * i, 15))

        if self.healthBar > 0:
            display.blit(assets.hudbar[1][0], (assets.playerIcon.get_width() + 10, 15))
            for i in range(1, self.healthBar):
                display.blit(assets.hudbar[1][1],
                             (assets.playerIcon.get_width() + 10 + assets.hudbar[0][1].get_width() * i, 15))


