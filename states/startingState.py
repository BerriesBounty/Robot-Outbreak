import pygame.font

from gfx import assets
from states.state import State


# the starting screen
class StartingState(State):
    def __init__(self, game):
        super().__init__(game)
        # stage 0 - press enter to start screen
        # 1 - main menu
        # 2 - start game
        # 3 - objective
        # 4 - controls
        self.curStage = 0  # the current stage of the starting screen it is in
        self.index = 0  # which option the player is hovering over in the main menu
        self.chosen = 0  # which option the player has chosen
        self.options = ["Start", "Objective", "Controls"]

        # the return to main menu button
        self.exitBox = pygame.surface.Surface((150, 50))
        self.exitBox.fill((92, 110, 153))  # fill the box with blue
        self.exitBox.set_alpha(200)  # make the box transparent
        self.exitRect = self.exitBox.get_rect(x=50, y=50)  # position it in the top left corner

    def tick(self):
        if self.curStage == 0:
            if self.game.inputManager.keyReleased.get("enter"):  # enter the main menu if player press enter
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
            if self.game.inputManager.keyReleased.get("enter"):  # go to the corresponding stage
                if self.index == 0:
                    self.curStage = 2
                elif self.index == 1:
                    self.curStage = 3
                else:
                    self.curStage = 4

        elif self.curStage == 2:  # if player chooses to start game
            self.game.gameState.start()  # prepare the gameState
            self.game.stateManager.set_state(self.game.gameState)  # change the current state to gameState

        # settings
        elif self.curStage == 3:
            if self.exitRect.collidepoint(self.game.inputManager.x, self.game.inputManager.y):  # if hovering exit box
                self.exitBox.set_alpha(50)
                if self.game.inputManager.mouseJustReleased[0]:
                    self.curStage = 1
            else:
                self.exitBox.set_alpha(200)

        # tutorial
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
                              self.game.height / 2, assets.fonts[2])  # render text in the center

        elif self.curStage == 1:
            image = assets.uiAssets[4].copy()  # the background image of the menu

            # the text boxes in the menu
            for i in range(3):
                if i == self.index:  # in the player is choosing this option
                    textbox = assets.uiAssets[6].copy()  # the lighter textbox
                else:
                    textbox = assets.uiAssets[5].copy()  # the darker box
                assets.renderFont(textbox, self.options[i], assets.white, assets.bgWhite, textbox.get_width() / 2 + 27,
                                  textbox.get_height() / 2, assets.fonts[1])  # write text on the box
                image.blit(textbox, (0, 120 + 60 * i + 5 * i))  # draw the box onto menu

            # draw the image in the middle
            renderRect = image.get_rect(center=(self.game.width / 2, self.game.height / 2))
            display.blit(image, renderRect)

            assets.renderFont(display, "Robot outbreak", assets.white, assets.bgWhite, self.game.width / 2,
                              self.game.height / 2 - 120, assets.fonts[1])  # draw the title of the game

            # draw the instruction for the controls
            instructionBox = assets.uiAssets[7].copy()
            display.blit(instructionBox, (self.game.width - (5 * 32 * 3 / 2), self.game.height / 2 - (2 * 32 * 3 / 2)))

        elif self.curStage == 3:
            # draw the exit box
            display.blit(self.exitBox, self.exitRect)
            assets.renderFont(display, "return", (134, 150, 190), (32, 51, 67), self.exitRect.centerx,
                              self.exitRect.centery, assets.fonts[2])

            # draw and write the objective
            image = assets.uiAssets[4].copy()
            assets.drawText(image, "Kill all enemies in a wave. Buy Items with money in between waves. Survive to win",
                            assets.white, (15, 120, 172 * (3 / 2), 136 * (3 / 2)),
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

            image = assets.uiAssets[4].copy()
            assets.drawText(image, "WASD to move. Right click to attack. Q to use special ability. "
                                   "1 and 2 to switch weapon", assets.white, (15, 120, 172 * (3 / 2), 136 * (3 / 2)),
                            assets.fonts[0])
            renderRect = image.get_rect(
                center=(self.game.width / 2, self.game.height / 2))
            display.blit(image, renderRect)
            assets.renderFont(display, "Tutorial", assets.white, assets.bgWhite, self.game.width / 2,
                              self.game.height / 2 - 120, assets.fonts[2])
