from gfx import assets
from bullets.enemyBullet import EnemyBullet
from weapons.weapon import Weapon


class EnemyAttack(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 20
        self.spread = 7
        self.rimage = assets.pistol[0]
        self.limage = assets.pistol[1]
        self.image = self.rimage
        self.rect = self.image.get_rect()
        self.xOffset = 2

    def attack(self):
        x = self.entity.enemies[0].rect.x
        y = self.entity.enemies[0].rect.y
        eBullet = EnemyBullet(self, x, y)
        eBullet.setxy(self.entity.rect.x + self.entity.rect.width / 2 - eBullet.rect.width / 2,
                      self.entity.rect.y + self.entity.rect.width / 2 - eBullet.rect.height / 2)
        self.entity.world.bullet_list.add(eBullet)
        assets.pistolSound[0].play()

    def update(self):
        self.rect.x = self.entity.rect.x + self.xOffset
        self.rect.y = self.entity.rect.y + 6

        if self.entity.direction == 0:
            curImage = self.rimage
            self.xOffset = -5
        else:
            curImage = self.limage
            self.xOffset = -25

        self.image = curImage

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.entity.world.state.game.gameCamera.xOffset,
                                  self.rect.y - self.entity.world.state.game.gameCamera.yOffset))
