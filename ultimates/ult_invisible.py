import time

from ultimates.ultimate import Ultimate

class Invisible(Ultimate):
    def __init__(self, duration, energy, id):
        super().__init__(duration, energy, id)

    def tick(self):
        self.timer += time.perf_counter() - self.lastTime
        self.lastTime = time.perf_counter()
        if self.timer >= self.duration:
            self.deactivate()
            return

        self.gamestate.world1.player.visible = False
        newImage = self.gamestate.world1.player.image.copy()
        newImage.set_alpha(100)
        self.gamestate.world1.player.image = newImage
        newGunImage = self.gamestate.world1.player.equippedWeapon.image.copy()
        newGunImage.set_alpha(100)
        self.gamestate.world1.player.equippedWeapon.image = newGunImage

    def activiate(self):
        self.lastTime = time.perf_counter()
        self.gamestate.world1.player.visible = False
        self.gamestate.world1.player.equippedWeapon.attackSpeed /= 1.25

    def deactivate(self):
        self.gamestate.world1.player.ultimateOn = False
        self.gamestate.world1.player.visible = False
        self.gamestate.world1.player.equippedWeapon.attackSpeed *= 1.25
        self.timer = 0
