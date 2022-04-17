import math
import random

import pygame

from gfx import assets


class Bullet(pygame.sprite.Sprite):
    def __init__(self, weapon, enemies, mx, my, spread):
        super().__init__()
        self.weapon = weapon
        self.enemies = enemies
        self.spread = spread
        self.image = assets.bullet
        self.rect = self.image.get_rect()
        self.mx = mx
        self.my = my
        self.damage = 1

    def setxy(self, x, y):
        self.rect.x = x
        self.rect.y = y
        diffx = self.mx - self.rect.x
        diffy = self.my - self.rect.y

        if diffx == 0:
            angle = 0
        else:
            angle = abs(math.atan(diffy/diffx)) + math.radians(random.randint(-self.spread * 10, self.spread * 10)/10)
        if diffx >= 0 and diffy <= 0:
            self.dx = 10.0 * math.cos(angle)
            self.dy = -10.0 * math.sin(angle)
        elif diffx < 0 and diffy <= 0:
            self.dx = -10.0 * math.cos(angle)
            self.dy = -10.0 * math.sin(angle)
        elif diffx >= 0 and diffy > 0:
            self.dx = 10.0 * math.cos(angle)
            self.dy = 10.0 * math.sin(angle)
        elif diffx < 0 and diffy > 0:
            self.dx = -10.0 * math.cos(angle)
            self.dy = 10.0 * math.sin(angle)


    def update(self):
        self.rect.y += self.dy
        self.rect.x += self.dx

        if self.rect.y + self.rect.height - self.weapon.entity.world.state.game.gameCamera.yOffset < 0 \
                or self.rect.x - self.rect.width - self.weapon.entity.world.state.game.gameCamera.xOffset < 0 or self.rect.x > 800:
            self.kill()
        self.checkCollision()

    def checkCollision(self):
        hit_list = pygame.sprite.spritecollide(self, self.enemies, False)
        for hit in hit_list:
            hit.hurt(self.weapon.damage)
            self.kill()

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.weapon.entity.world.state.game.gameCamera.xOffset,
                                  self.rect.y - self.weapon.entity.world.state.game.gameCamera.yOffset))