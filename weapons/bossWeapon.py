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
        x = self.entity.enemies[0].rect.x
        y = self.entity.enemies[0].rect.y
        eBullet = BossBullet(self, x, y)
        eBullet.setxy(self.entity.rect.x + self.entity.rect.width / 2 - eBullet.rect.width / 2,
                             self.entity.rect.y + self.entity.rect.width / 2 - eBullet.rect.height / 2)
        self.entity.world.bullet_list.add(eBullet)
        assets.pistolSound[0].play()

    def update(self):
        pass

    def render(self, display):
        pass
