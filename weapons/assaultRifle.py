import pygame

import assets
from bullet import Bullet
from weapons.weapon import Weapon


class AssaultRifle(Weapon):
    def __init__(self, entity, enemies):
        super().__init__(entity, enemies)
        self.attackSpeed = 0.25
        self.ogimage = assets.assaultRifle[3]
        # self.ogimage.set_colorkey(assets.purple)
        # self.image.blit(assets.hand, (15, 9))
        self.image = self.ogimage
        self.rect = self.ogimage.get_rect()

    def attack(self, x, y):
        bullet = Bullet(self.entity.world, x, y)
        bullet.setxy(self.entity.rect.x + self.entity.rect.width / 2 - bullet.rect.width / 2,
                        self.entity.rect.y - 16)
        self.entity.world.all_list.add(bullet)
        self.entity.world.bullet_list.add(bullet)

    def update(self):
        self.rect.x = self.entity.rect.x + 10
        self.rect.y = self.entity.rect.y + 10
        if self.entity.direction > 6:
            self.image = pygame.transform.rotate(self.ogimage, 30)
            self.image.set_colorkey(assets.purple)
        else:
            self.image = self.ogimage
            self.image.set_colorkey(assets.purple)

    def get_attackSpeed(self):
        return self.attackSpeed
