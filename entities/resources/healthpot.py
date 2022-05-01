import pygame
from pygame import display
from timer import Timer
from gfx import assets

class HealthDrop(pygame.sprite.Sprite):
    def __init__(self, world, x, y):
        super().__init__()
        self.world = world
        self.image = pygame.image.load('res/health.png')
        self.image = pygame.transform.scale(self.image,(32,32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.timer = Timer(10)

    def update(self):
        if self.timer.update():
            self.kill()
        if pygame.sprite.collide_rect(self.world.player, self):
            difference = self.world.player.maxHealth - self.world.player.health
            if difference < 5:
                self.world.player.health = self.world.player.maxHealth
            else:
                self.world.player.health += 5

            assets.resourceSound[1].play()
            self.kill()

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.world.state.game.gameCamera.xOffset,
                                      self.rect.y - self.world.state.game.gameCamera.yOffset))

