import time

from bullet import Bullet
from weapons.weapon import Weapon


class AssultRifle(Weapon):
    def __init__(self, entity, enemies):
        super().__init__(entity, enemies)
        self.attackSpeed = 0.25

    def attack(self):
        bullet = Bullet(self.entity.world, self.entity.world.game.get_inputManager().get_x(),
                            self.entity.world.game.get_inputManager().get_y())
        bullet.setxy(self.entity.rect.x + self.entity.rect.width / 2 - bullet.rect.width / 2,
                        self.entity.rect.y - 16)
        self.entity.world.all_list.add(bullet)
        self.entity.world.bullet_list.add(bullet)

    def update(self):
        pass

    def get_attackSpeed(self):
        return self.attackSpeed
