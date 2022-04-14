import math

from gfx import assets
from bullet import Bullet
from weapons.weapon import Weapon


class AssaultRifle(Weapon):
    def __init__(self, entity, enemies):
        super().__init__(entity, enemies)
        self.attackSpeed = 0.25
        self.damage = 1
        self.rimage = assets.assaultRifle[0]
        self.limage = assets.assaultRifle[1]

        self.image = self.rimage
        self.rect = self.image.get_rect()
        self.xOffset = 2
        self.rimage.blit(assets.hand, (self.rect.width / 2, self.rect.height / 2 - 2))
        self.limage.blit(assets.hand, (self.rect.width / 2 - 7, self.rect.height / 2 - 2))

    def attack(self):
        x = self.entity.world.state.game.inputManager.x
        y = self.entity.world.state.game.inputManager.y
        bullet = Bullet(self.enemies, x, y)
        bullet.setxy(self.entity.rect.x + self.entity.rect.width / 2 - bullet.rect.width / 2,
                        self.entity.rect.y + self.entity.rect.width / 2 - bullet.rect.height / 2)
        self.entity.world.all_list.add(bullet)
        self.entity.world.bullet_list.add(bullet)

    def update(self):
        self.rect.x = self.entity.rect.x + self.xOffset
        self.rect.y = self.entity.rect.y + 15

        if self.entity.direction == 0:
            curImage = self.rimage
            self.xOffset = 0
        else:
            curImage = self.limage
            self.xOffset = -20

        mx = self.entity.world.state.game.inputManager.x
        my = self.entity.world.state.game.inputManager.y
        dx = mx - self.rect.x
        dy = my - self.rect.y
        if dx == 0:
            dx = 0.01
        angle = -math.degrees(math.atan(dy/dx))
        if self.rect.x - 1 <= mx <= self.entity.rect.x:
            angle = -angle
        self.image = assets.rot_center(curImage, angle)
