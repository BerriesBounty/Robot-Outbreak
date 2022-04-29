import pygame
from pygame import display


class AmmoDrop():
    def __init__(self, x, y):
        self.image = pygame.image.load('res/ammo.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

    def render(self, surface):
        display.blit(self.image, (self.rect.x - self.world.state.game.gameCamera.xOffset,
                                      self.rect.y - self.world.state.game.gameCamera.yOffset))