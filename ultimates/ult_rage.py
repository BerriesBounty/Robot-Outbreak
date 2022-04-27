import time

import pygame.draw

from timer import Timer
from ultimates.ultimate import Ultimate

class Rage(Ultimate):
    def __init__(self, duration, energy, id):
        super().__init__(duration, energy, id)
        self.name = "Rage"
        self.description = "WHY DOESN'T THIS CODE WORK! WHY! (Gain increase fire rate and heal for each enemy killed)"
        self.timer = None
        self.lastKillAmount = None
        self.curKillAmount = None

    def tick(self):
        if self.timer.update():
            self.deactivate()
            return

        self.curKillAmount = self.player.kills
        print(self.curKillAmount,  self.lastKillAmount)
        if self.curKillAmount > self.lastKillAmount:
            self.player.health = min(self.player.maxHealth, self.player.health + 5)
            self.timer.timer -= 3
        self.lastKillAmount = self.player.kills


    def activiate(self):
        self.timer = Timer(self.duration)
        self.player.visible = False
        self.player.equippedWeapon.attackSpeed /= 1.5
        self.lastKillAmount = self.player.kills
        self.curKillAmount = self.player.kills

    def deactivate(self):
        self.player.ultimateOn = False
        self.player.equippedWeapon.attackSpeed *= 1.5
        self.timer = 0
