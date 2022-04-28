import math

import pygame

from gfx import assets
from bullets.bullet import Bullet, PierceBullet
from timer import Timer
from weapons.weapon import Weapon

class PiercingGun(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Piercing Gun"
        self.description = "Pew pew... pew pew pew... pewpewpew pewpewpew"
        self.attackSpeed = 1
        self.damage = 1
        self.spread = 4
        self.maxAmmo = 30
        self.ammo = 30
        self.magSize = 1
        self.curMag = 1
        self.reloadSpeed = 0.25
        self.timer = Timer(self.attackSpeed)

        self.rimage = assets.beam[0]
        self.limage = assets.beam[1]

        self.image = self.rimage
        self.rect = self.image.get_rect()
        self.xOffset = 2

    def attack(self):
        self.timer.update()
        if self.reloading:
            if self.timer.timer >= self.reloadSpeed:
                self.ammo -= min(self.ammo, self.magSize - self.curMag)
                self.curMag = min(self.magSize, self.ammo)
                self.timer.timer = self.attackSpeed
                self.reloading = False
        elif self.timer.timer < self.attackSpeed:  # instead of resetting timer to 0, we reset to the attack speed so it can be fired as soon as it finishes reloading
            return
        elif self.entity.world.state.game.inputManager.get_pressed(0):
            self.attacking = True
            if self.curMag == 0 and self.ammo == 0:
                self.entity.removeWeapon()
            else:
                x = self.entity.world.state.game.inputManager.offsetX - 90
                y = self.entity.world.state.game.inputManager.offsetY - 33

                bullet = PierceBullet(self, x, y)
                bullet.setxy(self.entity.rect.x + self.entity.rect.width / 2 - bullet.rect.width / 2,
                             self.entity.rect.y + self.entity.rect.width / 2 - bullet.rect.height / 2)
                self.entity.world.bullet_list.add(bullet)
                self.curMag -= 1
                assets.arSound[0].play()
                if self.curMag == 0:
                    self.reloading = True
                    assets.arSound[1].play()

            self.timer.reset()
        else:
            self.attacking = False

    def update(self):
        if self.entity.direction == 0:
            curImage = self.rimage
            self.xOffset = -20
        else:
            curImage = self.limage
            self.xOffset = -40

        if self.entity.canMove:
            self.rect.x = self.entity.rect.x + self.xOffset
            self.rect.y = self.entity.rect.y - 6

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

            if self.entity.world.state.game.inputManager.keyJustPressed.get("r"):
                self.reloading = True
                self.timer.reset()
                assets.arSound[1].play()
            self.attack()

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.entity.world.state.game.gameCamera.xOffset,
                                  self.rect.y - self.entity.world.state.game.gameCamera.yOffset))

