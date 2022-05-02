import pygame
from pygame import display
from timer import Timer
from gfx import assets

class AmmoDrop(pygame.sprite.Sprite):
    def __init__(self, world, x, y):
        super().__init__()
        self.world = world
        self.image = pygame.image.load('res/ammo.png')
        self.image = pygame.transform.scale(self.image,(32,32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.timer = Timer(10)

    def update(self):
        if self.timer.update():
            self.kill()
        if pygame.sprite.collide_rect(self.world.player, self):

            self.world.player.equippedWeapon.ammo = round(min(self.world.player.equippedWeapon.maxAmmo,
                                                        self.world.player.equippedWeapon.ammo + self.world.player.equippedWeapon.curMag
                                                        + (self.world.player.equippedWeapon.maxAmmo * 0.1)))
            assets.resourceSound[2].play()
            self.kill()

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.world.state.game.gameCamera.xOffset,
                                      self.rect.y - self.world.state.game.gameCamera.yOffset))

