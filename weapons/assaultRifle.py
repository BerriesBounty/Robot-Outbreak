import math
from gfx import assets
from bullets.bullet import Bullet
from timer import Timer
from weapons.weapon import Weapon


class AssaultRifle(Weapon):
    def __init__(self):
        super().__init__()
        self.name = "Assault rifle"
        self.description = "Pew pew... pew pew pew... pewpewpew pewpewpew"
        self.cost = 100
        self.attackSpeed = 0.11
        self.damage = 20
        self.spread = 4
        self.maxAmmo = 200
        self.ammo = 200
        self.magSize = 30
        self.curMag = 30
        self.reloadSpeed = 0.5
        self.timer = Timer(self.attackSpeed)  # timer to track the when to attack

        self.rimage = assets.assaultRifle[0]
        self.limage = assets.assaultRifle[1]

        self.image = self.rimage
        self.rect = self.image.get_rect()
        self.xOffset = -5  # where to display the image relative to the entity holding it

    def attack(self):
        self.timer.update()  # add time to timer
        if self.reloading:
            if self.timer.timer >= self.reloadSpeed:  # if finished reloading
                # subtract ammo from ammo and add to curMag. If ammo does not have enough, put all the ammo into
                ammoChange = min(self.ammo, self.magSize - self.curMag)
                self.curMag = min(self.magSize, self.ammo)
                self.ammo -= ammoChange
                self.timer.timer = self.attackSpeed  # it can shoot immediately after reloading
                self.reloading = False
        elif self.timer.timer < self.attackSpeed:  # if not enough time has passed yet
            return
        elif self.entity.world.state.game.inputManager.get_pressed(0):  # if the player is pressing down the left click
            self.attacking = True
            if self.curMag == 0:
                if self.ammo == 0:  # if the weapon lost all ammo, remove the weapon
                    self.entity.removeWeapon()
                else:
                    self.reloading = True
                    assets.arSound[1].play()  # play the reloading sound
            else:
                x = self.entity.world.state.game.inputManager.offsetX  # where the mouse is aiming at
                y = self.entity.world.state.game.inputManager.offsetY

                # create a bullet to aim at the mouse coming from the entity
                bullet = Bullet(self, x, y)
                bullet.setxy(self.entity.rect.x + self.entity.rect.width / 2 - bullet.rect.width / 2,
                             self.entity.rect.y + self.entity.rect.width / 2 - bullet.rect.height / 2)
                self.entity.world.bullet_list.add(bullet)
                self.curMag -= 1
                assets.arSound[0].play()
            self.timer.reset()  # restart the attack timer and set it to 0 again
        else:
            self.attacking = False

    def update(self):
        if self.entity.direction == 0:  # direction the entity is facing change which image to display
            curImage = self.rimage
            self.xOffset = -5
        else:
            curImage = self.limage
            self.xOffset = -25

        if self.entity.canMove:  # if the player can move, display the weapon to point at the cursor
            self.rect.x = self.entity.rect.x + self.xOffset  # make the weapon follow the player
            self.rect.y = self.entity.rect.y + 6

            mx = self.entity.world.state.game.inputManager.offsetX
            my = self.entity.world.state.game.inputManager.offsetY
            dx = mx - self.rect.x  # the adj and opp of the triangle formed with the cursor and weapon position
            dy = my - self.rect.y
            if dx == 0:  # make sure no division by 0
                dx = 0.01

            # if the mouse is in between the weapon image
            if self.rect.x < mx < self.rect.x + self.rect.width and self.entity.direction == 1:
                angle = math.degrees(math.atan(dy/dx))
            else:
                angle = -math.degrees(math.atan(dy/dx))  # find the angle needed to rotate the image
            self.image = assets.rot_center(curImage, angle)
            self.image.blit(assets.hand, (self.rect.width / 2 - 4, self.rect.height / 2 - 4))  # display the hand

            if self.entity.world.state.game.inputManager.keyJustPressed.get("r"):  # if the player wants to reload
                self.reloading = True
                self.timer.reset()
                assets.arSound[1].play()
            self.attack()

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.entity.world.state.game.gameCamera.xOffset,
                                  self.rect.y - self.entity.world.state.game.gameCamera.yOffset))
