from abc import ABC, abstractmethod

from pygame.sprite import Sprite


class Weapon(Sprite, ABC):
    def __init__(self, entity, enemies):
        super().__init__()
        self.attackSpeed = 1
        self.damage = 1
        self.ammo = 0
        self.magSize = 0
        self.curMag = 0
        self.reloadSpeed = 0
        self.reloading = False
        self.spread = 0

        self.entity = entity
        self.image = None
        self.rect = None
        self.enemies = enemies
        self.rimage = self.limage = None


    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def attack(self):
        pass

