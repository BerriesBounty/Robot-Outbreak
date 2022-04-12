from abc import ABC, abstractmethod

from pygame.sprite import Sprite


class Weapon(Sprite, ABC):
    def __init__(self, entity):
        super().__init__()
        self.attackSpeed = 1
        self.damage = 1
        self.entity = entity
        self.image = None
        self.rect = None

    @abstractmethod
    def update(self):
        pass
