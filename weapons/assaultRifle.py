import pygame

import assets
from bullet import Bullet
from weapons.weapon import Weapon


class AssaultRifle(Weapon):
    def __init__(self, entity, enemies):
        super().__init__(entity, enemies)
        self.attackSpeed = 0.25
        self.image = pygame.transform.scale(assets.assaultRifle, (35, 13))
        self.image.set_colorkey((98, 22, 107))
        self.image.blit(assets.hand, (10, 5))

        self.rect = self.image.get_rect()

    def attack(self):
        bullet = Bullet(self.entity.world, self.entity.world.game.get_inputManager().get_x(),
                            self.entity.world.game.get_inputManager().get_y())
        bullet.setxy(self.entity.rect.x + self.entity.rect.width / 2 - bullet.rect.width / 2,
                        self.entity.rect.y - 16)
        self.entity.world.all_list.add(bullet)
        self.entity.world.bullet_list.add(bullet)

    def update(self):
        self.rect.x = self.entity.rect.x + 8
        self.rect.y = self.entity.rect.y + 22

    def get_attackSpeed(self):
        return self.attackSpeed
