import time

from entities.creatures.decoy import Decoy
from gfx import assets
from timer import Timer
from ultimates.ultimate import Ultimate


class Invisible(Ultimate):
    def __init__(self, duration, energy):
        super().__init__(duration, energy)
        self.name = "Escape no Jutsu"
        self.description = "I will become the Hokage! (Become invisible and deploy a decoy to confuse the enemy)"
        self.cost = 100
        self.timer = None
        self.x = 0
        self.y = 0
        self.decoy = None

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

    def activate(self):
        assets.ultSound[1].play()
        self.timer = Timer(self.duration)
        self.player.visible = False
        self.decoy = Decoy(self.player.world, self.player.rect.x, self.player.rect.y)
        self.player.world.entityManager.add(self.decoy)


    def deactivate(self):
        self.player.ultimateOn = False
        self.player.visible = True
        self.timer = 0
        self.decoy.die()


