import random

from gfx import assets
from bullets.bossBullet import BossBullet
from weapons.weapon import Weapon


class EnemyAttack(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 25
        self.spread = 7
        self.rimage = assets.bossWeapon[0]
        self.limage = assets.bossWeapon[1]
        self.image = self.rimage
        self.rect = self.image.get_rect()
        self.xOffset = 2

    def attack(self):
        centerx = self.entity.rect.x + self.entity.rect.width / 2 - assets.bullet[2].get_width()
        centery = self.entity.rect.y + self.entity.rect.width / 2 - assets.bullet[2].get_height()
        bulletDirection = [[centerx, centery - 10], [centerx + 10, centery - 10], [centerx + 10, centery],
                           [centerx + 10, centery + 10], [centerx, centery + 10], [centerx - 10, centery + 10],
                           [centerx - 10, centery], [centerx - 10, centery - 10]]
        for pos in bulletDirection:
            eBullet = BossBullet(self, pos[0], pos[1])
            eBullet.setxy(centerx,
                          centery)
            self.entity.world.bullet_list.add(eBullet)
        assets.pistolSound[0].play()

    def update(self):
        pass

    def render(self, display):
        pass
