import math
import time

import pygame.rect

from gfx import assets
from weapons.weapon import Weapon


class Sword(Weapon):
    def __init__(self, entity):
        super().__init__(entity)
        self.attackSpeed = 1
        self.damage = 3
        self.rimage = assets.sword[0]
        self.limage = assets.sword[1]
        self.timer = self.attackSpeed
        self.lastTime = time.perf_counter()

        self.image = self.rimage
        self.rect = self.image.get_rect()
        self.xOffset = 2
        self.rimage.blit(assets.hand, (self.rect.width / 2 - 5, self.rect.height / 2 - 5))
        self.limage.blit(assets.hand, (self.rect.width / 2 - 5, self.rect.height / 2 - 5))

    def attack(self):
        self.timer += time.perf_counter() - self.lastTime
        self.lastTime = time.perf_counter()
        if self.timer < self.attackSpeed:
            return
        elif self.entity.world.state.game.inputManager.get_pressed(0):
            if self.entity.direction == 0:
                x = self.entity.rect.x + self.entity.rect.width
            else:
                x = self.entity.rect.x - 10
            attackRect = pygame.Rect((x, self.entity.rect.y), (10, self.entity.rect.height))
            hit_list = []
            for e in self.enemies:
                if attackRect.colliderect(e.rect):
                    hit_list.append(e)
            for hit in hit_list:
                hit.hurt(self.damage)
            self.timer = 0
        else:
            self.attacking = False

    def update(self):
        self.rect.x = self.entity.rect.x + self.xOffset
        self.rect.y = self.entity.rect.y - 12

        if self.entity.direction == 0:
            curImage = self.rimage
            self.xOffset = -20
        else:
            curImage = self.limage
            self.xOffset = -40

        mx = self.entity.world.state.game.inputManager.offsetX
        my = self.entity.world.state.game.inputManager.offsetY
        dx = mx - self.rect.x
        dy = my - self.rect.y
        if dx == 0:
            dx = 0.01
        if self.rect.x < mx < self.rect.x + self.rect.width and self.entity.direction == 1:
            angle = math.degrees(math.atan(dy / dx))
        else:
            angle = -math.degrees(math.atan(dy / dx))
        self.image = assets.rot_center(curImage, angle)

        self.attack()

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.entity.world.state.game.gameCamera.xOffset,
                                  self.rect.y - self.entity.world.state.game.gameCamera.yOffset))
