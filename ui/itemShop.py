import random

from gfx import assets
from ultimates import ultManager
from weapons.weaponManager import WeaponManager


class ItemShop:
    def __init__(self, world):
        self.world = world
        self.choices = []
        itemType = []
        itemType.append(random.randint(1, 2))
        itemType.append(random.randint(1, 2))
        for item in itemType:
            if item == 1:
                self.choices.append(random.choice(ultManager.ultimateList))
            elif item == 2:
                self.choices.append(random.choice(WeaponManager.weaponList))
        print(*self.choices)


    def tick(self):
        pass

    def render(self, display):
        display.blit(assets.uiAssets[0], (200, 100))
        for i in range(1, 9):
            display.blit(assets.uiAssets[1],
                         (200 + 32 * i, 100))
        display.blit(assets.uiAssets[2], (200 + 32 * 9, 100))
