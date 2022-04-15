import math
import time

from gfx import assets
from bullet import Bullet
from weapons.weapon import Weapon


class AssaultRifle(Weapon):
    def __init__(self, entity, enemies):
        super().__init__(entity, enemies)
        self.attackSpeed = 0.25
        self.damage = 1
        self.ammo = 120
        self.magSize = 20
        self.curMag = 10
        self.reloadSpeed = 3
        self.reloading = False
        self.timer = 0
        self.lastTime = time.perf_counter()

        self.rimage = assets.assaultRifle[0]
        self.limage = assets.assaultRifle[1]

        self.image = self.rimage
        self.rect = self.image.get_rect()
        self.xOffset = 2

    def attack(self):
        if self.curMag == 0:
            self.reloading = True
            assets.arSound[1].play()
            self.lastTime = time.perf_counter()
        else:
            x = self.entity.world.state.game.inputManager.x
            y = self.entity.world.state.game.inputManager.y
            bullet = Bullet(self.enemies, x, y)
            bullet.setxy(self.entity.rect.x + self.entity.rect.width / 2 - bullet.rect.width / 2,
                            self.entity.rect.y + self.entity.rect.width / 2 - bullet.rect.height / 2)
            self.entity.world.bullet_list.add(bullet)
            self.curMag -= 1
            assets.arSound[0].play()

    def update(self):
        self.rect.x = self.entity.rect.x + self.xOffset
        self.rect.y = self.entity.rect.y + 14

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
        if self.rect.x < mx < self.rect.x + self.rect.width and self.entity.direction == 1:
            angle = math.degrees(math.atan(dy/dx))
        else:
            angle = -math.degrees(math.atan(dy/dx))
        self.image = assets.rot_center(curImage, angle)
        self.image.blit(assets.hand, (self.rect.width / 2 - 4, self.rect.height / 2 - 4))

        if self.reloading:
            self.timer += time.perf_counter() - self.lastTime
            self.lastTime = time.perf_counter()
            if self.timer >= self.reloadSpeed:
                self.ammo -= self.magSize - self.curMag
                self.curMag = self.magSize
                self.timer = 0
                self.reloading = False

