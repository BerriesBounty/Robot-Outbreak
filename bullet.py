import math

import pygame

import assets


class Bullet(pygame.sprite.Sprite):
    def __init__(self, enemies, mx, my):
        super().__init__()
        self.enemies = enemies
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

        if diffx == 0:
            angle = 0
        else:
            angle = abs(math.atan(diffy/diffx))
        if diffx >= 0 and diffy <= 0:
            self.dx = 10.0 * math.cos(angle)
            self.dy = -10.0 * math.sin(angle)
        elif diffx < 0 and diffy <= 0:
            self.dx = -10.0 * math.cos(angle)
            self.dy = -10.0 * math.sin(angle)
        elif diffx >= 0 and diffy > 0:
            self.dx = 10.0 * math.cos(angle)
            self.dy = 10.0 * math.sin(angle)
        elif diffx < 0 and diffy > 0:
            self.dx = -10.0 * math.cos(angle)
            self.dy = 10.0 * math.sin(angle)


    def update(self):
        self.rect.y += self.dy
        self.rect.x += self.dx

        if self.rect.y < 0 - self.rect.height or self.rect.x - self.rect.width < 0 or self.rect.x > 800:
            self.kill()
        self.checkCollision()

    def checkCollision(self):
        hit_list = pygame.sprite.spritecollide(self, self.enemies, False)
        for hit in hit_list:
            hit.hurt(self.damage)
            self.kill()