from gfx import assets
from entities.creatures.creature import Creature
import random
import time
import pygame
from entities.creatures.player import Player
from weapons.enemyWeapon import  EnemyAttack
import math
from timer import Timer

class RangedEnemy(Creature):
    def __init__(self, world, health):
        super().__init__(world)
        self.image = assets.target
        self.rect = self.image.get_rect()
        self.health = health #by inputting the health value, we can account for the change in difficulty - more health with higher difficulty.
        self.animation_count = 0
        self.reset_offset = 0
        self.offset_x = random.randrange(-150, 150)
        self.offset_y = random.randrange(-150, 150) #the goal of the enemy is to attack the player and as such it will move towards the player, to add variety we have added the offset value so that for example if the player is at 0,0 -> the offset will cause the enemy to move towards a random point in that range - we will reset the offset randomly to offer that variability.
        self.timer = Timer(random.randint(1, 10))
        self.weapon = EnemyAttack()
        self.weapon.entity = self
        self.direction = 0
        self.enemies = [self.world.player]

    def setxy(self, x, y):
        self.rect.x = x
        self.rect.y = y




    def update(self):
        if self.timer.update() is True:
            self.timer = Timer(random.randint(1, 10))
            self.weapon.attack(self.entity.rect.x,self.entity.rect.y)

        reset_offset = random.randint(0,20)
        if reset_offset == 15:
            self.offset_x = random.randrange(-450, 450)
            self.offset_y = random.randrange(-450, 450)

        if self.health <= 0:
            self.world.player.kills += 1
            if len(self.world.target_list) == 1:
                self.world.waveCleared()
            self.kill()
        else:
            if self.world.player.rect.x + self.offset_x > self.rect.x:
                self.rect.x += 1
                self.direction = 0
            elif self.world.player.rect.x + self.offset_x < self.rect.x:
                self.rect.x -= 1
                self.direction = 1
            if self.world.player.rect.y + self.offset_y > self.rect.y:
                self.rect.y += 1
            elif self.world.player.rect.y + self.offset_y < self.rect.y:
                self.rect.y -= 1
        self.weapon.update()

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.world.state.game.gameCamera.xOffset,
                                  self.rect.y - self.world.state.game.gameCamera.yOffset))
        self.weapon.render(display)

    def die(self):
        pass



