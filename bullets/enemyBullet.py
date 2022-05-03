import math
import random

import pygame

from bullets.projectile import Projectile
from gfx import assets


class EnemyBullet(Projectile):
    def __init__(self, weapon, mx, my):
        super().__init__(weapon, mx, my)
        self.rImage = assets.bullet[2]
        self.lImage = assets.bullet[3]
        self.image = assets.bullet[2]
        self.rect = self.image.get_rect()
        self.damage = 5
        self.bulletSpeed = 7.5

    def checkdiff(self):
        if self.entity.difficulty == "easy":
            self.damage = 5
        elif self.entity.difficulty == "medium":
            self.damage = 7.5
        elif self.entity.difficulty == "hard":
            self.damage = 10

    def checkCollision(self):
        hit_list = pygame.sprite.spritecollide(self, self.entity.enemies, False)
        for hit in hit_list:
            hit.hurt(self.weapon.damage)
            assets.hurt.play()
            self.kill()

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.weapon.entity.world.state.game.gameCamera.xOffset,
                                  self.rect.y - self.weapon.entity.world.state.game.gameCamera.yOffset))