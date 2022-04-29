import pygame
from pygame import display


class MoneyDrop():
    def __init__(self, x, y):
        self.image = pygame.image.load('res/money.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



    def update(self):
        pass

    def render(self, surface):
        display.blit(self.image, (self.rect.x - self.world.state.game.gameCamera.xOffset,
                                      self.rect.y - self.world.state.game.gameCamera.yOffset))