import math
import random

import pygame

from gfx import assets


class SlashBullet(pygame.sprite.Sprite):
    def __init__(self, weapon, mx, my):
        super().__init__()
        self.weapon = weapon
        self.entity = self.weapon.entity
        self.spread = self.weapon.spread
        self.rImage = assets.slashBullet[0]
        self.lImage = assets.slashBullet[1]
        self.image = assets.bullet
        self.rect = self.image.get_rect()
        self.mx = mx
        self.my = my
        self.damage = 1

    def setxy(self, x, y):
        self.rect.x = x
        self.rect.y = y
        diffx = self.mx - self.rect.x
        diffy = self.my - self.rect.y
        if diffx < 0 :
            curImage = self.lImage
        else:
            curImage = self.rImage

        if diffx == 0:
            angle = 0
        else:
            angle = abs(math.atan(diffy/diffx)) + math.radians(random.randint(-self.spread * 10, self.spread * 10)/10)
        if diffx >= 0 and diffy <= 0:
            self.dx = 20.0 * math.cos(angle)
            self.dy = -20.0 * math.sin(angle)
        elif diffx < 0 and diffy <= 0:
            self.dx = -20.0 * math.cos(angle)
            self.dy = -20.0 * math.sin(angle)
        elif diffx >= 0 and diffy > 0:
            self.dx = 20.0 * math.cos(angle)
            self.dy = 20.0 * math.sin(angle)
        elif diffx < 0 and diffy > 0:
            self.dx = -20.0 * math.cos(angle)
            self.dy = 20.0 * math.sin(angle)

        dx = self.mx - self.rect.x
        dy = self.my - self.rect.y
        if dx == 0:
            dx = 0.01
        if self.rect.x < self.mx < self.rect.x + self.rect.width and self.entity.direction == 1:
            angle = math.degrees(math.atan(dy / dx))
        else:
            angle = -math.degrees(math.atan(dy / dx))
        self.image = pygame.transform.rotate(curImage, angle)


    def update(self):
        self.rect.y += self.dy
        self.rect.x += self.dx

        if self.rect.y + self.rect.height - self.weapon.entity.world.state.game.gameCamera.yOffset < 0 \
                or self.rect.x - self.rect.width - self.weapon.entity.world.state.game.gameCamera.xOffset < 0 or self.rect.x > 1600:
            self.kill()
        self.checkCollision()

    def checkCollision(self):
        hit_list = pygame.sprite.spritecollide(self, self.entity.enemies, False)
        for hit in hit_list:
            hit.hurt(self.weapon.damage)
            self.entity.energy = min(self.entity.energy + 5, 100)
            self.kill()

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.weapon.entity.world.state.game.gameCamera.xOffset,
                                  self.rect.y - self.weapon.entity.world.state.game.gameCamera.yOffset))