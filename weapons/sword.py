import math

import pygame.rect

from gfx import assets
from weapons.weapon import Weapon


class Sword(Weapon):
    def __init__(self, entity, enemies):
        super().__init__(entity, enemies)
        self.attackSpeed = 1
        self.damage = 3
        self.rimage = assets.sword[0]
        self.limage = assets.sword[1]

        self.image = self.rimage
        self.rect = self.image.get_rect()
        self.xOffset = 2
        self.rimage.blit(assets.hand, (self.rect.width / 2 - 5, self.rect.height / 2 - 5))
        self.limage.blit(assets.hand, (self.rect.width / 2 - 5, self.rect.height / 2 - 5))

    def attack(self):
        attackRect = pygame.Rect((self.entity.rect.x + self.entity.rect.width, self.entity.rect.y), (10, 10))
        hit_list = []
        for e in self.enemies:
            if attackRect.colliderect(e.rect):
                hit_list.append(e)
        for hit in hit_list:
            hit.hurt(self.damage)

    def update(self):
        self.rect.x = self.entity.rect.x + self.xOffset
        self.rect.y = self.entity.rect.y - 14

        if self.entity.direction == 0:
            curImage = self.rimage
            self.xOffset = -20
        else:
            curImage = self.limage
            self.xOffset = -40

        mx = self.entity.world.state.game.inputManager.x
        my = self.entity.world.state.game.inputManager.y
        dx = mx - self.rect.x + self.rect.width/2
        dy = my - self.rect.y + self.rect.height/2
        if dx == 0:
            dx = 0.01
        angle = -math.degrees(math.atan(dy / dx))
        if self.rect.x - 1 <= mx <= self.entity.rect.x:
            angle = -angle
        self.image = assets.rot_center(curImage, angle)
