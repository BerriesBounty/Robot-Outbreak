import random

import pygame

from gfx import assets
from ultimates.ultManager import UltManager
from upgrades.upgradeManager import UpgradeManager
from weapons.weapon import Weapon
from weapons.weaponManager import WeaponManager

#appears once a wave is cleared
class ItemShop:
    def __init__(self, world):
        self.world = world
        self.choices = []  # the four items the player can buy
        self.chosen = None  # what item the play bought
        itemType = [random.randint(1, 3), random.randint(1, 3), random.randint(1, 2), random.randint(1, 2)]
        for item in itemType:
            if item == 3:
                self.choices.append(random.choice(UltManager.ultimateList))
            elif item == 2:
                self.choices.append(random.choice(WeaponManager.weaponList))
            elif item == 1:
                self.choices.append(random.choice(UpgradeManager.upgradeList))
        self.index = 1
        self.stage = 0
        # 0 - choosing what to buy, 1 - bought weapon and need to replace one
        # 2 - bought ultimate and need to replace, 3 - bought soomething without needing to replace

        self.box = assets.uiAssets[3].copy()  # the message box after an item is bought
        self.boxRect = self.box.get_rect(
            center=(self.world.state.game.width / 2, self.world.state.game.height / 2))  # place in middle of screen
        self.msg = ""  # what message to display in the box
        self.msgRect = pygame.Rect(self.boxRect.x + 15, self.boxRect.y + 60, 140 * (3/2), 75 * (3/2))
        self.button = assets.buttons[0]  # the button to close the box
        # the rect of the button is smaller than the image bcs only part of the image is the actual button
        self.buttonRect = pygame.Rect(self.boxRect.x + (32 * 4 + 8) * (3 / 2), self.boxRect.y + 6 * (3 / 2),
                                      14 * (3 / 2), 14 * (3 / 2))

    def tick(self):
        if self.stage == 0: # if the player is still choosing
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
            if self.world.state.game.inputManager.keyReleased.get("enter"):  # player has chosen
                self.chosen = self.choices[self.index]
                if self.chosen in WeaponManager.weaponList:  # if the player bought a weapon
                    if len(self.world.player.weapons) < 2:  # if the player only had one weapon
                        self.chosen.entity = self.world.player
                        self.world.player.weapons.append(self.chosen)  # give the player the weapon bought
                        self.successfulPurchase()
                    else:
                        #let them choose to replace a weapon
                        self.msg = f"Choose a weapon to replace: press 1 - {self.world.player.weapons[0].name}, 2 - {self.world.player.weapons[1].name}, or close the window"
                        self.stage = 1

                if self.chosen in UltManager.ultimateList:  # if the player chose an ultimate
                    if self.world.player.ultimate is None:  # if the plaer did not have a ultimate
                        self.chosen.player = self.world.player
                        self.world.player.ultimate = self.chosen
                        self.successfulPurchase()
                    else:
                        # let them choose to keep the one they had or to replace it
                        self.msg = f"{self.chosen.name} will replace {self.world.player.ultimate.name}, press enter to commit. If not, close the window"
                        self.stage = 2

                if self.chosen in UpgradeManager.upgradeList:  # if they choose an upgrade
                    self.chosen.player = self.world.player
                    self.chosen.activate()  #activate the upgrade
                    self.successfulPurchase()

        else:
            if self.stage == 1:
                if self.world.state.game.inputManager.keyReleased.get("1"):
                    self.chosen.entity = self.world.player
                    self.world.player.weapons[0] = self.chosen
                    self.world.player.equippedWeapon = self.world.player.weapons[0]
                    self.stage = 3
                if self.world.state.game.inputManager.keyReleased.get("2"):
                    self.chosen.entity = self.world.player
                    self.world.player.weapons[1] = self.chosen
                    self.world.player.equippedWeapon = self.world.player.weapons[1]
                    self.stage = 3

            elif self.stage == 2:
                if self.world.state.game.inputManager.keyReleased["enter"]:
                    self.chosen.player = self.world.player
                    self.world.player.ultimate = self.chosen
                    self.stage = 3
                if self.buttonRect.collidepoint(self.world.state.game.inputManager.x, self.world.state.game.inputManager.y):
                    self.button = assets.buttons[1]
                    if self.world.state.game.inputManager.mouse[0]:
                        self.button = assets.buttons[2]
                    if self.world.state.game.inputManager.mouseJustReleased[0]:
                        self.world.timer = None
                        self.world.stage += 1
                        self.world.player.canMove = True
                        self.world.waveStart()

            if self.buttonRect.collidepoint(self.world.state.game.inputManager.x, self.world.state.game.inputManager.y):
                self.button = assets.buttons[1]
                if self.world.state.game.inputManager.mouse[0]:
                    self.button = assets.buttons[2]
                if self.world.state.game.inputManager.mouseJustReleased[0]:
                    self.world.timer = None
                    self.world.stage += 1
                    self.world.player.canMove = True
                    self.world.waveStart()
            if self.world.state.game.inputManager.keyReleased.get("enter"):
                self.world.timer = None
                self.world.stage += 1
                self.world.player.canMove = True
                self.world.waveStart()
            else:
                self.button = assets.buttons[0]

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
                                  textbox.get_height()/2, assets.fonts[1])
                image.blit(textbox, (0, 120 + 60 * i + 3 * i))

            renderRect = assets.uiAssets[0].get_rect(
                center=(self.world.state.game.width / 2, self.world.state.game.height / 2))
            display.blit(assets.uiAssets[0], renderRect)

            assets.renderFont(display, "Item Shop", (229, 229, 242), (68, 68, 97), self.world.state.game.width / 2,
                              self.world.state.game.height / 2 - 150, assets.fonts[2])
        else:
            self.box.blit(self.button, (32 * 4 * (3 / 2), 0))  # display the x button
            display.blit(self.box, self.boxRect)
            assets.drawText(display, self.msg, (229, 229, 242), self.msgRect, assets.fonts[0])


    def successfulPurchase(self):
        self.msg = "Thanks for purchasing, now please just die."
        self.stage = 3
