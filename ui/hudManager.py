import math

from gfx import assets


class HUDManager():
    def __init__(self, world):
        self.world = world
        self.player = self.world.player
        self.healthBar = 10
        self.ammoBar = 10
        self.energyBar = 10

    def tick(self):
        self.healthBar = math.ceil(self.player.health / self.player.maxHealth * 10)
        if self.player.equippedWeapon is not None:
            self.ammoBar = math.ceil(((self.player.equippedWeapon.ammo + self.player.equippedWeapon.curMag)
                                  / (self.player.equippedWeapon.maxAmmo + self.player.equippedWeapon.magSize)) * 10)
        else:
            self.ammoBar = 10
        self.energyBar = math.ceil((self.player.energy / self.player.maxEnergy) * 10)

    def render(self, display):
        display.blit(assets.hudAssets[0], (10, 10))

        # health bar ---------------------------------------------------------------*
        display.blit(assets.hudBar[0][0], (assets.hudAssets[0].get_width() + 10, 14))
        for i in range(1, 10):
            display.blit(assets.hudBar[0][1],
                         (assets.hudAssets[0].get_width() + 10 + assets.hudBar[0][1].get_width() * i, 14))

        if self.healthBar > 0:
            display.blit(assets.hudBar[1][0], (assets.hudAssets[0].get_width() + 10, 14))
            for i in range(1, self.healthBar):
                display.blit(assets.hudBar[1][1],
                             (assets.hudAssets[0].get_width() + 10 + assets.hudBar[0][1].get_width() * i, 14))
        # Energy bar -----------------------------------------------------------------*
        display.blit(assets.hudBar[0][0], (assets.hudAssets[0].get_width() + 10, 34))
        for i in range(1, 10):
            display.blit(assets.hudBar[0][1],
                         (assets.hudAssets[0].get_width() + 10 + assets.hudBar[0][1].get_width() * i, 34))

        if self.energyBar > 0:
            display.blit(assets.hudBar[2][0], (assets.hudAssets[0].get_width() + 10, 34))
            for i in range(1, self.energyBar):
                display.blit(assets.hudBar[2][1],
                             (assets.hudAssets[0].get_width() + 10 + assets.hudBar[0][1].get_width() * i, 34))
        # Green Bar ------------------------------------------------------------------*
        display.blit(assets.hudBar[0][0], (assets.hudAssets[0].get_width() + 10, 54))
        for i in range(1, 10):
            display.blit(assets.hudBar[0][1],
                         (assets.hudAssets[0].get_width() + 10 + assets.hudBar[0][1].get_width() * i, 54))

        if self.ammoBar > 0:
            display.blit(assets.hudBar[3][0], (assets.hudAssets[0].get_width() + 10, 54))
            for i in range(1, self.ammoBar):
                display.blit(assets.hudBar[3][1],
                             (assets.hudAssets[0].get_width() + 10 + assets.hudBar[0][1].get_width() * i, 54))
        # end of health bars
        display.blit(assets.hudAssets[1],
                     (assets.hudAssets[0].get_width() + assets.hudBar[0][0].get_width() * 10 + 10, 10))

        # current weapon magazine
        if self.player.equippedWeapon is not None and self.player.equippedWeapon.maxAmmo != -1:
            assets.renderFont(display, f"{self.player.equippedWeapon.curMag}/{self.player.equippedWeapon.ammo}"
                              , (255, 0, 0), (172, 50, 50),
                              self.world.state.game.width - 100, self.world.state.game.height - 100, assets.fonts[2])

        #wave number
        assets.renderFont(display, f"wave number {self.world.wave}", (200, 0, 0), (172, 50, 50),
                          self.world.state.game.width - 200,
                          50, assets.fonts[2])

        # money
        assets.renderFont(display, f"${self.player.money}", (0, 200, 0), (50, 170, 50),
                          self.world.state.game.width - 100,
                          self.world.state.game.height - 150, assets.fonts[2])

        #ultimate
        if self.player.ultimate is not None and self.player.energy == self.player.maxEnergy:
            assets.renderFont(display, "Ultimate (Q)", (64, 147, 153), (13, 91, 170),
                              self.world.state.game.width - 150,
                              self.world.state.game.height - 200, assets.fonts[2])