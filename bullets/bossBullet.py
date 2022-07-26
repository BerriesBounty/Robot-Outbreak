import math
import random

import pygame

from bullets.projectile import Projectile
from gfx import assets
from gfx.tiles import Tile


class BossBullet(Projectile):
    def __init__(self, weapon, mx, my):
        super().__init__(weapon, mx, my)
        self.rImage = assets.bullet[2]
        self.lImage = assets.bullet[3]
        self.image = assets.bullet[2]
        self.rImage = pygame.transform.scale(self.rImage, (50, 50))
        self.lImage = pygame.transform.scale(self.lImage, (50, 50))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.damage = 5
        self.bulletSpeed = 7.5
        self.bounce = 2  # how many times the bullet bounces

    def checkdiff(self):
        if self.entity.difficulty == "easy":
            self.damage = 3
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