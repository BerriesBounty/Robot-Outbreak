from abc import ABC, abstractmethod

from pygame.sprite import Sprite


class Weapon(Sprite, ABC):
    def __init__(self, entity, enemies):
        super().__init__()
        self.attackSpeed = 1
        self.damage = 1
        self.entity = entity
        self.image = None
        self.rect = None
        self.enemies = enemies
        self.rimage = self.limage = None
        self.ammo = 0

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, display):
        pass
