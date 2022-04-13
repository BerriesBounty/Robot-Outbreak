import math

import pygame

import assets
from bullet import Bullet
from weapons.weapon import Weapon


class AssaultRifle(Weapon):
    def __init__(self, entity, enemies):
        super().__init__(entity, enemies)
        self.attackSpeed = 0.25
        self.rimage = assets.assaultRifle[0]
        self.limage = assets.assaultRifle[1]
        # self.ogimage.set_colorkey(assets.purple)
        # self.image.blit(assets.hand, (15, 9))
        self.image = self.rimage
        self.rect = self.image.get_rect()

    def attack(self, x, y):
        bullet = Bullet(self.enemies, x, y)
        bullet.setxy(self.entity.rect.x + self.entity.rect.width / 2 - bullet.rect.width / 2,
                        self.entity.rect.y - 16)
        self.entity.world.all_list.add(bullet)
        self.entity.world.bullet_list.add(bullet)

    def update(self):
        self.rect.x = self.entity.rect.x + 2
        self.rect.y = self.entity.rect.y + 8

        if self.entity.direction == 0:
            curImage = self.rimage
            self.image.set_colorkey(assets.purple)
        else:
            curImage = self.limage
            self.image.set_colorkey(assets.purple)

        mx = self.entity.world.get_state().get_game().get_inputManager().get_x()
        my = self.entity.world.get_state().get_game().get_inputManager().get_y()
        dx = abs(mx - self.rect.x)
        dy = my - self.rect.y
        angle = math.atan(dx/dy)
        self.image = assets.rot_center(curImage, angle)


    def get_attackSpeed(self):
        return self.attackSpeed
