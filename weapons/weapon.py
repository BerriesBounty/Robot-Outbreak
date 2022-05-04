from abc import ABC, abstractmethod

from pygame.sprite import Sprite


class Weapon(Sprite, ABC):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.description = ""
        self.cost = 0  # how much gold is needed to buy this item
        self.attackSpeed = 1  # time between each attack in second
        self.damage = 1
        self.maxAmmo = 0
        self.ammo = 0
        self.magSize = 10
        self.curMag = 10  # current magazine
        self.reloadSpeed = 0  # how long it takes to reload
        self.reloading = False
        self.attacking = False
        self.spread = 0  # the bullet guns shoot out will be varied a couple of degrees based on the spread

        self.entity = None  # the entity using the weapon
        self.image = None
        self.rect = None
        self.rimage = self.limage = None  # the image for facing left and right

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, display):
        pass

    @abstractmethod
    def attack(self):
        pass

