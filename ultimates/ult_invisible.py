import time

from timer import Timer
from ultimates.ultimate import Ultimate

class Invisible(Ultimate):
    def __init__(self, duration, energy, id):
        super().__init__(duration, energy, id)
        self.name = "Invisibility"
        self.timer = None

    def tick(self):
        if self.timer.update():
            self.deactivate()
            return

        newImage = self.player.image.copy()
        newImage.set_alpha(100)
        self.player.image = newImage
        newGunImage = self.player.equippedWeapon.image.copy()
        newGunImage.set_alpha(100)
        self.player.equippedWeapon.image = newGunImage

    def activiate(self):
        self.timer = Timer(self.duration)
        self.player.visible = False
        self.player.equippedWeapon.attackSpeed /= 1.25

    def deactivate(self):
        self.player.ultimateOn = False
        self.player.visible = False
        self.player.equippedWeapon.attackSpeed *= 1.25
        self.timer = 0
