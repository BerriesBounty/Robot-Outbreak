from abc import ABC, abstractmethod


class Upgrade(ABC):
    def __init__(self):
        self.player = None
        self.name = ""

    @abstractmethod
    def activate(self):
        pass


class HealthPack(Upgrade):
    def __init__(self):
        self.name = "Health Pack"

    def activate(self):
        self.player.health = min(self.player.maxHealth, self.player.health + 20)


class AmmoPack(Upgrade):
    def __init__(self):
        self.name = "Ammo Pack"

    def activate(self):
        self.player.equippedWeapon.ammo = round(min(self.player.equippedWeapon.maxAmmo,
                                                    self.player.equippedWeapon.ammo + self.player.equippedWeapon.curMag + (
                                                            self.player.equippedWeapon.maxAmmo * 0.25)))