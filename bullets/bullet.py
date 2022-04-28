import math
import random

import pygame

from bullets.projectile import Projectile
from gfx import assets


class Bullet(Projectile):
    def __init__(self, weapon, mx, my):
        super().__init__(weapon, mx, my)
        self.rImage = assets.bullet[0]
        self.lImage = assets.bullet[1]
        self.image = assets.bullet[0]
        self.rect = self.image.get_rect()
        self.damage = 1
        self.bulletSpeed = 20

    def checkCollision(self):
        hit_list = pygame.sprite.spritecollide(self, self.entity.enemies, False)
        for hit in hit_list:
            hit.hurt(self.weapon.damage)
            self.entity.energy = min(self.entity.energy + 5, self.entity.maxEnergy)
            self.kill()

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.weapon.entity.world.state.game.gameCamera.xOffset,
                                  self.rect.y - self.weapon.entity.world.state.game.gameCamera.yOffset))

class PierceBullet(Projectile):
    def __init__(self, weapon, mx, my):
        super().__init__(weapon, mx, my)
        self.rImage = assets.bullet[4]
        self.lImage = assets.bullet[5]
        self.image = assets.bullet[4]
        self.rect = self.image.get_rect()
        self.damage = 1
        self.bulletSpeed = 40

    def checkCollision(self):
        hit_list = pygame.sprite.spritecollide(self, self.entity.enemies, False)
        for hit in hit_list:
            hit.hurt(self.weapon.damage)
            self.entity.energy = min(self.entity.energy + 5, self.entity.maxEnergy)

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.weapon.entity.world.state.game.gameCamera.xOffset,
                                  self.rect.y - self.weapon.entity.world.state.game.gameCamera.yOffset))