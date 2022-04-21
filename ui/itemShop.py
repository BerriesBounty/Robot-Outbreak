import random

from gfx import assets
from ultimates.ultManager import UltManager
from upgrades.upgradeManager import UpgradeManager
from weapons.weapon import Weapon
from weapons.weaponManager import WeaponManager


class ItemShop:
    def __init__(self, world):
        self.world = world
        self.choices = []
        itemType = [random.randint(1, 3), random.randint(1, 3), random.randint(1, 2), random.randint(1, 2)]
        for item in itemType:
            if item == 1:
                self.choices.append(random.choice(UltManager.ultimateList))
            elif item == 2:
                self.choices.append(random.choice(WeaponManager.weaponList))
            elif item == 3:
                self.choices.append(random.choice(UpgradeManager.upgradeList))
        self.index = 1
        self.stage = 0

    def tick(self):
        if self.stage == 0:
            if self.world.state.game.inputManager.keyJustPressed.get("down"):
                if self.index == 3:
                    self.index = 0
                else:
                    self.index += 1
            if self.world.state.game.inputManager.keyJustPressed.get("up"):
                if self.index == 0:
                    self.index = 3
                else:
                    self.index -= 1
            if self.world.state.game.inputManager.keyReleased.get("enter"):
                self.stage += 1
        else:
            chosen = self.choices[self.index]
            if chosen in WeaponManager.weaponList: #if the player bought a weapon
                if len(self.world.player.weapons) < 2:
                    chosen.entity = self.world.player
                    self.world.player.weapons.append(chosen)
                    self.world.timer = None
                    self.world.player.canMove = True
                    self.world.stage += 1
            if chosen in UltManager.ultimateList:
                if self.world.player.ultimate is None:
                    chosen.player = self.world.player
                    self.world.player.ultimate = chosen
                    self.world.timer = None
                    self.world.player.canMove = True
                    self.world.stage += 1
            if chosen in UpgradeManager.upgradeList:
                chosen.player = self.world.player
                chosen.activate()
                self.world.timer = None
                self.world.player.canMove = True
                self.world.stage += 1

    def render(self, display):
        if self.stage == 0:
            image = assets.uiAssets[0]

            # the four rectangle boxes
            for i in range(4):
                if i == self.index:
                    textbox = assets.uiAssets[2].copy()
                else:
                    textbox = assets.uiAssets[1].copy()
                assets.renderFont(textbox, self.choices[i].name, (229, 229, 242), (68, 68, 97), textbox.get_width()/2 + 27,
                                  textbox.get_height()/2, assets.font18)
                image.blit(textbox, (0, 120 + 60 * i + 3 * i))

            renderRect = assets.uiAssets[0].get_rect(
                center=(self.world.state.game.width / 2, self.world.state.game.height / 2))
            display.blit(assets.uiAssets[0], renderRect)

            assets.renderFont(display, "Item Shop", (229, 229, 242), (68, 68, 97), self.world.state.game.width / 2,
                              self.world.state.game.height / 2 - 150, assets.font36)
        else:
            pass
