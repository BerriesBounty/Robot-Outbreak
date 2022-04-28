import math

import pygame.rect

from gfx import assets
from gfx.animation import Animation
from bullets.slashBullet import SlashBullet
from timer import Timer
from weapons.weapon import Weapon


class CoolSword(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Cooler Sword"
        self.description = "Hey, this sword is all shiny and stuff, that must mean it's good, right?"
        self.maxAmmo = -1
        self.attackSpeed = 0.25
        self.damage = 3
        self.rimage = assets.coolSword[0]
        self.limage = assets.coolSword[1]
        self.timer = Timer(self.attackSpeed)

        self.image = self.rimage
        self.rect = self.image.get_rect()
        self.xOffset = 2
        self.rimage.blit(assets.hand, (self.rect.width / 2 - 5, self.rect.height / 2 - 5))
        self.limage.blit(assets.hand, (self.rect.width / 2 - 5, self.rect.height / 2 - 5))
        self.slash = Animation(0.035, assets.swordSlash, 1)

    def attack(self):
        if not self.timer.update():
            return
        elif self.entity.world.state.game.inputManager.get_pressed(0):
            self.attacking = True
            self.slash.reset()

            if self.entity.direction == 0:
                x = self.entity.rect.x + self.entity.rect.width
            else:
                x = self.entity.rect.x - 64
            attackRect = pygame.Rect((x, self.entity.rect.y), (64, self.entity.rect.height))
            hit_list = []
            for e in self.entity.enemies:
                if attackRect.colliderect(e.rect):
                    hit_list.append(e)
            for hit in hit_list:
                hit.hurt(self.damage)
                self.entity.energy = min(self.entity.energy + 5, 100)

            x = self.entity.world.state.game.inputManager.offsetX - 32
            y = self.entity.world.state.game.inputManager.offsetY - 32
            bullet = SlashBullet(self, x, y)
            bullet.setxy(self.entity.rect.x + self.entity.rect.width / 2 - bullet.rect.width / 2,
                         self.entity.rect.y + self.entity.rect.width / 2 - bullet.rect.height / 2)
            self.entity.world.bullet_list.add(bullet)
            assets.pistolSound[0].play()

            self.timer.reset()
        else:
            self.attacking = False

    def update(self):
        if self.attacking:
            self.slash.tick()
            if self.entity.direction == 0:
                curImage = self.rimage
                self.xOffset = 20
            else:
                curImage = self.limage
                self.xOffset = -40
        else:
            if self.entity.direction == 0:
                curImage = self.rimage
                self.xOffset = -20
            else:
                curImage = self.limage
                self.xOffset = -40
        self.rect.x = self.entity.rect.x + self.xOffset
        self.rect.y = self.entity.rect.y - 12

        if self.entity.canMove:
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
        display.blit(self.getAnimationFrame(), (self.rect.x - self.entity.world.state.game.gameCamera.xOffset,
                                  self.rect.y - self.entity.world.state.game.gameCamera.yOffset))

    def getAnimationFrame(self):
        if self.attacking and self.slash.loops != 0:
            if self.entity.direction == 0:
                return self.slash.getCurrentFrame()
            else:
                return pygame.transform.flip(self.slash.getCurrentFrame(), True, False)
        else:
            self.attacking = False
            return self.image
