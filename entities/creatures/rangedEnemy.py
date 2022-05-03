from entities.resources.ammo import AmmoDrop
from entities.resources.money import MoneyDrop
from gfx import assets
from entities.creatures.creature import Creature
import random
import time
import pygame
from entities.creatures.player import Player
from gfx.animation import Animation
from weapons.enemyWeapon import  EnemyAttack
import math
from entities.resources.healthpot import HealthDrop
from timer import Timer

class RangedEnemy(Creature):
    def __init__(self, world, difficulty):
        super().__init__(world)
        self.walkingRight = Animation(0.15, assets.meleeEnemyWalkingRight, 0)
        self.walkingLeft = Animation(0.15, assets.meleeEnemyWalkingLeft, 0)
        self.image = assets.meleeEnemyWalkingLeft[0]
        self.rect = self.image.get_rect()
        self.difficulty = difficulty
        self.health = 0
        self.checkdiff()
        self.animation_count = 0
        self.reset_offset = 0
        self.offset_x = random.randrange(-450, 450)
        self.offset_y = random.randrange(-450, 450) #the goal of the enemy is to attack the player and as such it will move towards the player, to add variety we have added the offset value so that for example if the player is at 0,0 -> the offset will cause the enemy to move towards a random point in that range - we will reset the offset randomly to offer that variability.
        self.timer = Timer(random.randint(1, 7))
        self.weapon = EnemyAttack()
        self.weapon.entity = self
        self.direction = 0
        self.enemies = [self.world.player]


    def checkdiff(self):
        if self.difficulty == "easy":
            self.health = 80
        elif self.difficulty == "medium":
            self.health = 75
        elif self.difficulty == "hard":
            self.health = 100
    def setxy(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.walkingLeft.tick()
        self.walkingRight.tick()

        if self.timer.update() is True:
            self.timer = Timer(random.randint(1, 7))
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
            if self.world.player.rect.x + self.offset_x > self.rect.x:
                self.xmove += 1
                self.direction = 0
            elif self.world.player.rect.x + self.offset_x < self.rect.x:
                self.xmove -= 1
                self.direction = 1
            if self.world.player.rect.y + self.offset_y > self.rect.y:
                self.ymove += 1
            elif self.world.player.rect.y + self.offset_y < self.rect.y:
                self.ymove -= 1
            self.move()
        self.weapon.update()

    def render(self, display):
        display.blit(self.getCurrentAnimation(), (self.rect.x - self.world.state.game.gameCamera.xOffset,
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

    def getCurrentAnimation(self):
        if self.xmove > 0:
            return self.walkingRight.getCurrentFrame()
        else:
            return self.walkingLeft.getCurrentFrame()



