from gfx import assets
from entities.creatures.creature import Creature
import random
import pygame
from weapons.bossWeapon import  EnemyAttack
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
        self.reset_offset = 0
        self.offset_x = random.randrange(-450, 450)
        self.offset_y = random.randrange(-450, 450) #the goal of the enemy is to attack the player and as such it will move towards the player, to add variety we have added the offset value so that for example if the player is at 0,0 -> the offset will cause the enemy to move towards a random point in that range - we will reset the offset randomly to offer that variability.
        self.timer = Timer(random.randint(1, 3))
        self.weapon = EnemyAttack()
        self.weapon.entity = self
        self.direction = 0
        self.enemies = [self.world.player]


    def setxy(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):

        if self.timer.update() is True:
            self.timer = Timer(random.randint(1, 3))
            self.weapon.attack()

        reset_offset = random.randint(0,20)
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





