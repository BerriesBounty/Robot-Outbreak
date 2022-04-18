import time

from ultimates.ultimate import Ultimate


class Invisible(Ultimate):
    def __init__(self, game, duration, energy):
        super().__init__(game, duration, energy)

    def tick(self):
        self.timer += time.perf_counter() - self.lastTime
        self.lastTime = time.perf_counter()
        if self.timer >= self.duration:
            self.gamestate.world.player.ultimateOn = False
            self.gamestate.world.player.visible = True
            self.timer = 0
            return

        self.gamestate.world.player.visible = False
        newImage = self.gamestate.world.player.image.copy()
        newImage.set_alpha(100)
        self.gamestate.world.player.image = newImage
        newGunImage = self.gamestate.world.player.equippedWeapon.image.copy()
        newGunImage.set_alpha(100)
        self.gamestate.world.player.equippedWeapon.image = newGunImage