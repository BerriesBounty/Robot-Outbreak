import time

import pygame.rect

import assets
from weapons.weapon import Weapon


class Sword(Weapon):
    def __init__(self, entity, enemies):
        super().__init__(entity, enemies)
        self.attackSpeed = 1
        self.damage = 3
        self.image = assets.sword
        self.rect = self.image.get_rect()

    def attack(self):
        attackRect = pygame.Rect((self.entity.rect.x + self.entity.rect.width, self.entity.rect.y), (10, 10))
        hit_list = []
        for e in self.enemies:
            if attackRect.colliderect(e.rect):
                hit_list.append(e)
        for hit in hit_list:
            hit.hurt(self.damage)

    def update(self):
        self.rect.x = self.entity.rect.x + self.entity.rect.width/2
        self.rect.y = self.entity.rect.y

    def get_attackSpeed(self):
        return self.attackSpeed
