from abc import ABC, abstractmethod

import pygame

from gfx import assets


class Upgrade(ABC):
    def __init__(self):
        self.player = None
        self.name = ""
        self.description = ""
        self.cost = 0

    @abstractmethod
    def activate(self):
        pass


class HealthPack(Upgrade):
    def __init__(self):
        self.name = "Blood Bag"
        self.description = "Look at all those dead bodies you just created... " \
                           "It would be a shame if all those fresh blood goes to waste. (Heal 20 health)"
        self.cost = 20

    def activate(self):
        self.player.health = min(self.player.maxHealth, self.player.health + 20)


class AmmoPack(Upgrade):
    def __init__(self):
        self.name = "Ammo Pack"
        self.description = "It's just ammo, nothing interesting to say about it (gain 25% of ammo for your equipped weapon)"
        self.cost = 20

    def activate(self):
        self.player.equippedWeapon.ammo = round(min(self.player.equippedWeapon.maxAmmo,
                                                    self.player.equippedWeapon.ammo + self.player.equippedWeapon.curMag
                                                    + (self.player.equippedWeapon.maxAmmo * 0.25)))

class MaxHealthUp(Upgrade):
    def __init__(self):
        self.name = "Apple"
        self.description = "An Apple a day keeps the doctors away (Increase max health by 20)"
        self.cost = 25

    def activate(self):
        self.player.maxHealth += 20

