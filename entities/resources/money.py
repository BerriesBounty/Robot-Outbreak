import random

import pygame
from pygame import display

from gfx import assets
from timer import Timer

class MoneyDrop(pygame.sprite.Sprite):
    def __init__(self, world, x, y):
        super().__init__()
        self.world = world
        self.image = pygame.image.load('res/money.png')
        self.image = pygame.transform.scale(self.image,(32,32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.timer = Timer(10)

    def update(self):
        if self.timer.update():
            self.kill()
        if pygame.sprite.collide_rect(self.world.player, self):
            num = random.randint(1,100)
            if num == 1:
                self.world.player.money += 100
            else:
                self.world.player.money += random.randint(5,20)
            assets.resourceSound[0].play()
            self.kill()

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.world.state.game.gameCamera.xOffset,
                                      self.rect.y - self.world.state.game.gameCamera.yOffset))

