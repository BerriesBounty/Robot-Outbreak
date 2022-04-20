from gfx import assets
from entities.creatures.creature import Creature
import random
import time
import pygame
import

class RangedAttack():
    def __init__(self,x,y,radius,facing,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.facing = facing
        self.color = color
        self.vel = 8 * facing
    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

class MeleeEnemy(Creature):
    def __init__(self, world, health, x, y):
        super().__init__(world)
        self.image = assets.target
        self.rect = self.image.get_rect()
        self.health = health #by inputting the health value, we can account for the change in difficulty - more health with higher difficulty.
        self.x = x
        self.y = y
        self.animation_count = 0
        self.reset_offset = 0
        self.offset_x = random.randrange(-150, 150)
        self.offset_y = random.randrange(-150, 150) #the goal of the enemy is to attack the player and as such it will move towards the player, to add variety we have added the offset value so that for example if the player is at 0,0 -> the offset will cause the enemy to move towards a random point in that range - we will reset the offset randomly to offer that variability.

    def update(self):
        if self.health <= 0:
            self.kill()

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.world.state.game.gameCamera.xOffset,
                                  self.rect.y - self.world.state.game.gameCamera.yOffset))

    def die(self):
        pass

class RangedEnemy(Creature):
    def __init__(self, world, health, x, y):
        super().__init__(world)
        self.image = assets.target
        self.rect = self.image.get_rect()
        self.health = health #by inputting the health value, we can account for the change in difficulty - more health with higher difficulty.
        self.x = x
        self.y = y
        self.animation_count = 0
        self.reset_offset = 0
        self.offset_x = random.randrange(-150, 150)
        self.offset_y = random.randrange(-150, 150) #the goal of the enemy is to attack the player and as such it will move towards the player, to add variety we have added the offset value so that for example if the player is at 0,0 -> the offset will cause the enemy to move towards a random point in that range - we will reset the offset randomly to offer that variability.

    def attack(self, difficulty):
        if difficulty == "easy":
            countdown = random.randint(0,9)
            while True:
                projectiles = []
                countdown += 1
                time.sleep(1)
                if countdown == 10: #counter will determine how frequently enemy shoots.

        if difficulty == "medium":
            countdown = random.randint(0,6)
            while True:
                countdown += 1
                time.sleep(1)
                if countdown == 7:
                    pass
        if difficulty == "hard":
            countdown = random.randint(0,3)
            while True:
                countdown += 1
                time.sleep(1)
                if countdown == 4:
                    pass

    def update(self):
        if self.health <= 0:
            self.kill()

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.world.state.game.gameCamera.xOffset,
                                  self.rect.y - self.world.state.game.gameCamera.yOffset))

    def die(self):
        pass



