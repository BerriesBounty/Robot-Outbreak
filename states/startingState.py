import pygame.font

from gfx import assets
from states.state import State


# the starting screen
class StartingState(State):
    def __init__(self, game):
        super().__init__(game)
        self.curStage = 0  # the current stage of the starting screen it is in
        self.index = 0  # which option the player is hovering over in the main menu
        self.chosen = 0  # which option the player has chosen
        self.options = ["Start", "Settings", "Tutorial"]

        # the return to main menu button
        self.exitBox = pygame.surface.Surface((150, 50))
        self.exitBox.fill((92, 110, 153))  # fill the box with blue
        self.exitBox.set_alpha(200)  # make the box transparent
        self.exitRect = self.exitBox.get_rect(x=50, y=50)  # position it in the top left corner

    def tick(self):
        if self.curStage == 0:
            if self.game.inputManager.keyReleased.get("enter"):
                self.curStage = 1
        elif self.curStage == 1:
            if self.game.inputManager.keyJustPressed.get("down"):
                if self.index == 2:
                    self.index = 0
                else:
                    self.index += 1
            if self.game.inputManager.keyJustPressed.get("up"):
                if self.index == 0:
                    self.index = 2
                else:
                    self.index -= 1

            if self.game.inputManager.keyReleased.get("enter"):
                if self.index == 0:
                    self.curStage = 2
                elif self.index == 1:
                    self.curStage = 3
                else:
                    self.curStage = 4
        elif self.curStage == 2:  # if player chooses to start game
            self.game.gameState.start()
            self.game.stateManager.set_state(self.game.gameState)
        elif self.curStage == 3:
            if self.exitRect.collidepoint(self.game.inputManager.x, self.game.inputManager.y):
                self.exitBox.set_alpha(50)
                if self.game.inputManager.mouseJustReleased[0]:
                    self.curStage = 1
            else:
                self.exitBox.set_alpha(200)
        elif self.curStage == 4:
            if self.exitRect.collidepoint(self.game.inputManager.x, self.game.inputManager.y):
                self.exitBox.set_alpha(50)
                if self.game.inputManager.mouseJustReleased[0]:
                    self.curStage = 1
            else:
                self.exitBox.set_alpha(200)


    def render(self, display):
        if self.curStage == 0:
            assets.renderFont(display, "PRESS ENTER TO START", assets.white, assets.bgWhite, self.game.width / 2,
                        self.game.height / 2, assets.fonts[2])
        elif self.curStage == 1:
            image = assets.uiAssets[5].copy()

            for i in range(3):
                if i == self.index:
                    textbox = assets.uiAssets[7].copy()
                else:
                    textbox = assets.uiAssets[6].copy()
                assets.renderFont(textbox, self.options[i], assets.white, assets.bgWhite, textbox.get_width()/2 + 27,
                                  textbox.get_height()/2, assets.fonts[1])
                image.blit(textbox, (0, 120 + 60 * i + 5 * i))

            renderRect = image.get_rect(
                center=(self.game.width / 2, self.game.height / 2))
            display.blit(image, renderRect)

            assets.renderFont(display, "SUS", assets.white, assets.bgWhite, self.game.width / 2,
                              self.game.height / 2 - 120, assets.fonts[2])

            instructionBox = assets.uiAssets[8].copy()
            display.blit(instructionBox, (self.game.width - (5 * 32 * 3/2), self.game.height / 2 - (2 * 32 * 3/2)))


        elif self.curStage == 3:
            display.blit(self.exitBox, self.exitRect)
            assets.renderFont(display, "return", (134, 150, 190), (32, 51, 67), self.exitRect.centerx,
                              self.exitRect.centery, assets.fonts[2])

            image = assets.uiAssets[5].copy()
            assets.drawText(image, "Kill all enemies in a wave. Buy Items with money in between waves. Survive to win", assets.white, (15, 120, 172 * (3 / 2), 136 * (3 / 2)),
                            assets.fonts[0])
            renderRect = image.get_rect(
                center=(self.game.width / 2, self.game.height / 2))
            display.blit(image, renderRect)
            assets.renderFont(display, "Tutorial", assets.white, assets.bgWhite, self.game.width / 2,
                              self.game.height / 2 - 120, assets.fonts[2])
        elif self.curStage == 4:
            display.blit(self.exitBox, self.exitRect)
            assets.renderFont(display, "return", (134, 150, 190), (32, 51, 67), self.exitRect.centerx,
                              self.exitRect.centery, assets.fonts[2])

            image = assets.uiAssets[5].copy()
            assets.drawText(image, "WASD to move. Right click to attack. Q to use special ability. "
                                   "1 and 2 to switch weapon", assets.white, (15, 120, 172 * (3/2), 136 * (3/2)), assets.fonts[0])
            renderRect = image.get_rect(
                center=(self.game.width / 2, self.game.height / 2))
            display.blit(image, renderRect)
            assets.renderFont(display, "Tutorial", assets.white, assets.bgWhite, self.game.width / 2,
                             self.game.height / 2 - 120, assets.fonts[2])
