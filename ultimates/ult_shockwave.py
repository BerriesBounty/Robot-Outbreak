import time

from timer import Timer
from ultimates.ultimate import Ultimate

class Shockwave(Ultimate):
    def __init__(self, duration, energy, id):
        super().__init__(duration, energy, id)
        self.name = "Shockwave"
        self.description = "Ew, don't touch me! (Destroy all bullets in the room)"
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

    def activiate(self):
        self.timer = Timer(self.duration)

    def deactivate(self):
        pass
