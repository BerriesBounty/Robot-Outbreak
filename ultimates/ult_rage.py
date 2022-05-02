import time

import pygame.draw

from gfx import assets
from timer import Timer
from ultimates.ultimate import Ultimate


class Rage(Ultimate):
    def __init__(self, duration, energy):
        super().__init__(duration, energy)
        self.name = "Rage"
        self.description = "WHY DOESN'T THIS CODE WORK! WHY! (Gain increase fire rate and heal for each enemy killed)"
        self.cost = 125
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
            self.player.health = min(self.player.maxHealth, self.player.health + 10)
            self.timer.timer -= 3
        self.lastKillAmount = self.player.kills

    def activate(self):
        assets.ultSound[2].play()
        self.timer = Timer(self.duration)
        self.player.visible = False
        self.player.equippedWeapon.attackSpeed /= 1.5
        self.lastKillAmount = self.player.kills
        self.curKillAmount = self.player.kills

    def deactivate(self):
        self.player.ultimateOn = False
        self.player.equippedWeapon.attackSpeed *= 1.5
        self.timer = 0
