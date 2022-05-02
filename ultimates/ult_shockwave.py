import time

from gfx import assets
from timer import Timer
from ultimates.ultimate import Ultimate


class Shockwave(Ultimate):
    def __init__(self, duration, energy):
        super().__init__(duration, energy)
        self.name = "Shockwave"
        self.description = "Ew, don't touch me! (Destroy all bullets in the room)"
        self.cost = 50
        self.timer = None

    def tick(self):
        if self.timer.update():
            self.deactivate()
            return

        for i in self.player.world.bullet_list:
            if i.weapon.entity == self.player:
                continue
            else:
                i.kill()

    def activate(self):
        assets.ultSound[0].play()
        self.timer = Timer(self.duration)

    def deactivate(self):
        pass
