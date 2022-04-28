import pygame.font

from gfx import assets
from states.state import State


class StartingState(State):
    def __init__(self, game):
        super().__init__(game)
        self.curStage = 0
        self.index = 0
        self.chosen = 0
        self.options = ["Start", "Settings", "Tutorial"]
        self.exitBox = pygame.surface.Surface((150, 50))
        self.exitBox.fill((136, 206, 242))
        self.exitBox.set_alpha(25)
        self.exitRect = self.exitBox.get_rect(x=50,y=50)

    def tick(self):
        pass
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
                self.exitBox.set_alpha(25)
        elif self.curStage == 4:
            if self.exitRect.collidepoint(self.game.inputManager.x, self.game.inputManager.y):
                self.exitBox.set_alpha(50)
                if self.game.inputManager.mouseJustReleased[0]:
                    self.curStage = 1
            else:
                self.exitBox.set_alpha(25)


    def render(self, display):
        if self.curStage == 0:
            assets.renderFont(display, "PRESS ENTER TO START", (229, 229, 242), (68, 68, 97), self.game.width / 2,
                        self.game.height / 2, assets.fonts[2])
        elif self.curStage == 1:
            image = assets.uiAssets[5]

            for i in range(3):
                if i == self.index:
                    textbox = assets.uiAssets[7].copy()
                else:
                    textbox = assets.uiAssets[6].copy()
                assets.renderFont(textbox, self.options[i], (229, 229, 242), (68, 68, 97), textbox.get_width()/2 + 27,
                                  textbox.get_height()/2, assets.fonts[1])
                image.blit(textbox, (0, 120 + 60 * i + 5 * i))

            renderRect = assets.uiAssets[5].get_rect(
                center=(self.game.width / 2, self.game.height / 2))
            display.blit(assets.uiAssets[5], renderRect)

            assets.renderFont(display, "SUS", (229, 229, 242), (68, 68, 97), self.game.width / 2,
                              self.game.height / 2 - 120, assets.fonts[2])
        elif self.curStage == 3:
            assets.renderFont(display, "Just deal with the current", (229, 229, 242), (68, 68, 97), self.game.width / 2,
                              self.game.height / 2, assets.fonts[2])
            assets.renderFont(display, "settings lmao", (229, 229, 242), (68, 68, 97), self.game.width / 2,
                              self.game.height / 2 + 50, assets.fonts[2])

            display.blit(self.exitBox, self.exitRect)
            msg = assets.fonts[2].render("return", False, (32, 51, 67))
            msgRect = msg.get_rect(center=self.exitRect.center)
            display.blit(msg, msgRect)
        elif self.curStage == 4:
            display.blit(self.exitBox, self.exitRect)
            msg = assets.fonts[2].render("return", False, (32, 51, 67))
            msgRect = msg.get_rect(center=self.exitRect.center)
            display.blit(msg, msgRect)

