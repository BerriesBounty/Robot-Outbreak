import math

from gfx import assets
from bullets.bullet import Bullet
from timer import Timer
from weapons.weapon import Weapon


class Pistol(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Pistol"
        self.description = "It's a gun and it works. It might not be the best, but what other choice do you have?" \
                           " (hint: the other three options)"
        self.cost = 50
        self.attackSpeed = 0.25
        self.damage = 20
        self.spread = 7
        self.maxAmmo = 20
        self.ammo = 20
        self.magSize = 10
        self.curMag = self.magSize
        self.reloadSpeed = 1.2
        self.timer = Timer(self.attackSpeed)

        self.rimage = assets.pistol[0]
        self.limage = assets.pistol[1]

        self.image = self.rimage
        self.rect = self.image.get_rect()
        self.xOffset = 2

    def attack(self):
        self.timer.update()
        if self.reloading:
            if self.timer.timer >= self.reloadSpeed:
                reloadAmmo = min(self.ammo, self.magSize - self.curMag)
                self.ammo -= reloadAmmo
                self.curMag = reloadAmmo
                self.timer.timer = self.attackSpeed
                self.reloading = False

        elif self.timer.timer < self.attackSpeed:
            return
        elif self.entity.world.state.game.inputManager.get_pressed(0):
            self.attacking = True
            if self.curMag == 0:
                if self.ammo == 0:
                    self.entity.removeWeapon()
                else:
                    self.reloading = True
                    assets.pistolSound[1].play()
            else:
                x = self.entity.world.state.game.inputManager.offsetX - 22
                y = self.entity.world.state.game.inputManager.offsetY - 17
                bullet = Bullet(self, x, y)
                bullet.setxy(self.entity.rect.x + self.entity.rect.width / 2 - bullet.rect.width / 2,
                             self.entity.rect.y + self.entity.rect.width / 2 - bullet.rect.height / 2)
                self.entity.world.bullet_list.add(bullet)
                self.curMag -= 1
                assets.pistolSound[0].play()
            self.timer.reset()
        else:
            self.attacking = False

    def update(self):
        self.rect.x = self.entity.rect.x + self.xOffset
        self.rect.y = self.entity.rect.y + 6

        if self.entity.direction == 0:
            curImage = self.rimage
            self.xOffset = -5
        else:
            curImage = self.limage
            self.xOffset = -25

        if self.entity.canMove:
            mx = self.entity.world.state.game.inputManager.offsetX
            my = self.entity.world.state.game.inputManager.offsetY
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

            if self.entity.world.state.game.inputManager.keyJustPressed.get("r"):
                self.reloading = True
                self.timer.reset()
                assets.pistolSound[1].play()
            self.attack()

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.entity.world.state.game.gameCamera.xOffset,
                                  self.rect.y - self.entity.world.state.game.gameCamera.yOffset))

