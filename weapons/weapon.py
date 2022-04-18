from abc import ABC, abstractmethod

from pygame.sprite import Sprite


class Weapon(Sprite, ABC):
    def __init__(self, entity):
        super().__init__()
        self.attackSpeed = 1
        self.damage = 1
        self.maxAmmo = 0
        self.ammo = 0
        self.magSize = 10
        self.curMag = 10
        self.reloadSpeed = 0
        self.reloading = False
        self.attacking = False
        self.spread = 0

        self.entity = entity
        self.image = None
        self.rect = None
        self.enemies = self.entity.enemies
        self.rimage = self.limage = None


    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, display):
        pass

    @abstractmethod
    def attack(self):
        pass

