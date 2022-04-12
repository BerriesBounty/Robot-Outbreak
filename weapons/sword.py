import time

import pygame.rect

import assets
from weapons.weapon import Weapon


class Sword(Weapon):
    def __init__(self, entity, enemies):
        super().__init__(entity, enemies)
        self.attackSpeed = 0.25
        self.damage = 3
        self.image = assets.cannon
        self.rect = pygame.Rect((self.entity.rect.x + self.entity.rect.width, self.entity.rect.y),
                                       (18, 26))

    def attack(self):
        self.attactRect = pygame.Rect((self.entity.rect.x + self.entity.rect.width, self.entity.rect.y),
                                      (50, 50))

        hit_list = []
        for e in self.enemies:
            if self.attactRect.colliderect(e.rect):
                hit_list.append(e)
        for hit in hit_list:
            hit.hurt(self.damage)

    def update(self):
        self.rect.x = self.entity.rect.x + self.entity.rect.width
        self.rect.y = self.entity.rect.y

    def get_attackSpeed(self):
        return self.attackSpeed
