import math

from gfx import assets


class HUDManager():
    def __init__(self, world):
        self.world = world
        self.player = self.world.player
        self.healthBar = 10
        self.ammoBar = 10

    def tick(self):
        self.healthBar = math.ceil(self.player.health / 10)
        self.ammoBar = math.ceil((self.player.equippedWeapon.curMag / self.player.equippedWeapon.magSize) * 10)

    def render(self, display):
        display.blit(assets.hudAssets[0], (10, 10))

        # health bar ---------------------------------------------------------------*
        display.blit(assets.hudbar[0][0], (assets.hudAssets[0].get_width() + 10, 14))
        for i in range(1, 10):
            display.blit(assets.hudbar[0][1],
                         (assets.hudAssets[0].get_width() + 10 + assets.hudbar[0][1].get_width() * i, 14))

        if self.healthBar > 0:
            display.blit(assets.hudbar[1][0], (assets.hudAssets[0].get_width() + 10, 14))
            for i in range(1, self.healthBar):
                display.blit(assets.hudbar[1][1],
                             (assets.hudAssets[0].get_width() + 10 + assets.hudbar[0][1].get_width() * i, 14))
        # Energy bar -----------------------------------------------------------------*
        display.blit(assets.hudbar[0][0], (assets.hudAssets[0].get_width() + 10, 34))
        for i in range(1, 10):
            display.blit(assets.hudbar[0][1],
                         (assets.hudAssets[0].get_width() + 10 + assets.hudbar[0][1].get_width() * i, 34))

        if self.healthBar > 0:
            display.blit(assets.hudbar[2][0], (assets.hudAssets[0].get_width() + 10, 34))
            for i in range(1, self.healthBar):
                display.blit(assets.hudbar[2][1],
                             (assets.hudAssets[0].get_width() + 10 + assets.hudbar[0][1].get_width() * i, 34))
        # Green Bar ------------------------------------------------------------------*
        display.blit(assets.hudbar[0][0], (assets.hudAssets[0].get_width() + 10, 54))
        for i in range(1, 10):
            display.blit(assets.hudbar[0][1],
                         (assets.hudAssets[0].get_width() + 10 + assets.hudbar[0][1].get_width() * i, 54))

        if self.ammoBar > 0:
            display.blit(assets.hudbar[3][0], (assets.hudAssets[0].get_width() + 10, 54))
            for i in range(1, self.ammoBar):
                display.blit(assets.hudbar[3][1],
                             (assets.hudAssets[0].get_width() + 10 + assets.hudbar[0][1].get_width() * i, 54))
        #end of health bars
        display.blit(assets.hudAssets[1],
                     (assets.hudAssets[0].get_width() + assets.hudbar[0][0].get_width() * 10 + 10, 10))

