import pygame


class Inventory:
    def __init__(self, world):
        self.world = world
        self.items = []
        self.isActive = False

    def tick(self):
        if self.world.state.game.inputManager.keyJustPressed[pygame.K_TAB]:
            self.isActive = not self.isActive
        if not self.isActive:
            return


