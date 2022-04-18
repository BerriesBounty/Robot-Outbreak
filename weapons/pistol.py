import math
import time

import pygame

from gfx import assets
from bullet import Bullet
from weapons.weapon import Weapon
import random as rnd

class Pistol(Weapon):
    def __init__(self, entity):
        super().__init__(entity)
        self.attackSpeed = 0.25
        self.damage = 2
        self.spread = 7
        self.maxAmmo = 140
        self.ammo = 140
        self.magSize = 10
        self.curMag = self.magSize
        self.reloadSpeed = 1.2
        self.timer = self.attackSpeed
        self.lastTime = time.perf_counter()

        self.rimage = assets.pistol[0]
        self.limage = assets.pistol[1]

        self.image = self.rimage
        self.rect = self.image.get_rect()
        self.xOffset = 2

    def attack(self):
        self.timer += time.perf_counter() - self.lastTime
        self.lastTime = time.perf_counter()
        if self.reloading:
            if self.timer >= self.reloadSpeed:
                self.ammo -= min(self.ammo, self.magSize - self.curMag)
                self.curMag = min(self.magSize, self.ammo)
                self.timer = self.attackSpeed
                self.reloading = False

        elif self.timer < self.attackSpeed:
            return
        elif self.entity.world.state.game.inputManager.get_pressed(0):
            self.attacking = True
            if self.curMag == 0:
                if self.ammo == 0:
                    return
                else:
                    self.reloading = True
                    assets.pistolSound[1].play()
            else:
                x = self.entity.world.state.game.inputManager.offsetX
                y = self.entity.world.state.game.inputManager.offsetY
                bullet = Bullet(self, x, y)
                bullet.setxy(self.entity.rect.x + self.entity.rect.width / 2 - bullet.rect.width / 2,
                             self.entity.rect.y + self.entity.rect.width / 2 - bullet.rect.height / 2)
                self.entity.world.bullet_list.add(bullet)
                self.curMag -= 1
                assets.pistolSound[0].play()
            self.timer = 0
        else:
            self.attacking = False

    def update(self):
        self.rect.x = self.entity.rect.x + self.xOffset
        self.rect.y = self.entity.rect.y + 6

        if self.entity.direction == 0:
            curImage = self.rimage
            self.xOffset = -5
        else:
            curImage = self.limage
            self.xOffset = -25

        mx = self.entity.world.state.game.inputManager.offsetX
        my = self.entity.world.state.game.inputManager.offsetY
        dx = mx - self.rect.x
        dy = my - self.rect.y
        if dx == 0:
            dx = 0.01
        if self.rect.x < mx < self.rect.x + self.rect.width and self.entity.direction == 1:
            angle = math.degrees(math.atan(dy/dx))
        else:
            angle = -math.degrees(math.atan(dy/dx))
        self.image = assets.rot_center(curImage, angle)
        self.image.blit(assets.hand, (self.rect.width / 2 - 4, self.rect.height / 2 - 4))

        if self.entity.world.state.game.inputManager.keyJustPressed[pygame.K_r]:
            self.reloading = True
            self.timer = 0
            assets.pistolSound[1].play()
        self.attack()

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.entity.world.state.game.gameCamera.xOffset,
                                  self.rect.y - self.entity.world.state.game.gameCamera.yOffset))

