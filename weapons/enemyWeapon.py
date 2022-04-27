import math
import time

import pygame
from gfx import assets
from enemyBullet import EnemyBullet
from bullet import Bullet
from timer import Timer
from weapons.weapon import Weapon
import random as rnd

class EnemyAttack(Weapon):
    def __init__(self):
        super().__init__()
        self.attackSpeed = 0.25
        self.damage = 2
        self.spread = 7
        self.timer = Timer(self.attackSpeed)
        self.rimage = assets.pistol[0]
        self.limage = assets.pistol[1]
        self.image = self.rimage
        self.rect = self.image.get_rect()
        self.xOffset = 2

    def attack(self):
        x = self.world.player.rect.x
        y = self.world.player.rect.y
        bullet = EnemyBullet(self, x, y)
        bullet.setxy(self.entity.rect.x + self.entity.rect.width / 2 - bullet.rect.width / 2,
                             self.entity.rect.y + self.entity.rect.width / 2 - bullet.rect.height / 2)
        self.entity.world.bullet_list.add(bullet)
        assets.pistolSound[0].play()

    def update(self):
        self.rect.x = self.entity.rect.x + self.xOffset
        self.rect.y = self.entity.rect.y + 6

        if self.entity.direction == 0:
            curImage = self.rimage
            self.xOffset = -5
        else:
            curImage = self.limage
            self.xOffset = -25

        self.image = curImage

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.entity.world.state.game.gameCamera.xOffset,
                                  self.rect.y - self.entity.world.state.game.gameCamera.yOffset))

