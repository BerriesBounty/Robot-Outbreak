from gfx import assets
from entities.creatures.creature import Creature
import random
import pygame
from weapons.bossWeapon import EnemyAttack
from entities.resources.healthpot import HealthDrop
from entities.resources.ammo import AmmoDrop
from entities.resources.money import MoneyDrop
from timer import Timer


class FinalBoss(Creature):
    def __init__(self, world):
        super().__init__(world)
        self.image = assets.boss
        self.rect = self.image.get_rect()
        self.maxHealth = 1500
        self.health = 1500

        # same AI as enemies
        self.reset_offset = 0  # when to change the offset
        self.offset_x = random.randrange(-450, 450)
        self.offset_y = random.randrange(-450, 450)
        self.timer = Timer(random.randint(2, 5))
        self.moveTimer = None
        self.weapon = EnemyAttack()
        self.weapon.entity = self
        self.direction = 0
        self.enemies = [self.world.player]
        self.canMove = True

    def setxy(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # when the boss attacks, it will stop moving. The move timer checks how long the boss has stopped moving
        # if it finishes, let the boss move and attack again. Set move timer to none so it doesn't update again
        if self.moveTimer is not None and self.moveTimer.update():
            self.timer.reset()
            self.moveTimer = None
            self.canMove = True

        # when the boss attacks, it stops moving
        if self.timer.update():  # if allowed attacking
            self.moveTimer = Timer(2)  # stop the boss from moving
            self.timer.reset()
            self.canMove = False
            self.weapon.attack()

        reset_offset = random.randint(0, 20)  # 1/20 chance to reset the offset of the boss
        if reset_offset == 15:
            self.offset_x = random.randrange(-450, 450)
            self.offset_y = random.randrange(-450, 450)

        if self.health <= 0:
            self.die()
            self.world.player.kills += 1
            if len(self.world.target_list) == 1:
                self.world.waveCleared()
            self.kill()
        else:
            self.xmove = 0
            self.ymove = 0
            if self.enemies[0].rect.x + self.offset_x > self.rect.x:
                self.xmove += 7
                self.direction = 0
            elif self.enemies[0].rect.x + self.offset_x < self.rect.x:
                self.xmove -= 7
                self.direction = 1
            if self.enemies[0].rect.y + self.offset_y > self.rect.y:
                self.ymove += 7
            elif self.enemies[0].rect.y + self.offset_y < self.rect.y:
                self.ymove -= 7

            if self.canMove:
                self.move()
        hit_list = pygame.sprite.spritecollide(self, self.enemies, False)
        for hit in hit_list:
            hit.hurt(5)
        self.weapon.update()

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.world.state.game.gameCamera.xOffset,
                                  self.rect.y - self.world.state.game.gameCamera.yOffset))
        self.weapon.render(display)

    def die(self):
        resource = random.randint(1, 100)
        if resource <= 10:
            health = HealthDrop(self.world, self.rect.x, self.rect.y)
            self.world.resource_list.add(health)
        elif resource <= 60:
            self.world.resource_list.add(MoneyDrop(self.world, self.rect.x, self.rect.y))
        elif resource <= 70:
            self.world.resource_list.add(AmmoDrop(self.world, self.rect.x, self.rect.y))
        else:
            pass





