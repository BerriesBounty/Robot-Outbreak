import time
import pygame
import assets
from entities.creatures.creature import Creature
from weapons.assaultRifle import AssaultRifle
from weapons.sword import Sword


class Player(Creature):
    def __init__(self, world):
        super().__init__(world)
        self.left = pygame.transform.scale(assets.leftCannon, (36, 48))
        self.right = pygame.transform.scale(assets.rightCannon, (36, 48))
        self.center = pygame.transform.scale(assets.cannon, (36, 48))
        self.image = self.center
        self.rect = self.image.get_rect()
        self.setxy()
        self.direction = 0  # direction of clock

        self.weapon = AssaultRifle(self, self.world.target_list)
        self.attackSpeed = self.weapon.get_attackSpeed()
        self.lastAttack = time.perf_counter()
        self.attackTimer = self.attackSpeed
        self.attacking = False

        self.world.all_list.add(self)
        self.world.all_list.add(self.weapon)

    def setxy(self):
        self.rect.x = self.world.get_state().get_game().width / 2 - self.rect.width / 2
        self.rect.y = self.world.get_state().get_game().height - self.rect.height

    def update(self):
        self.getInput()
        if self.direction == 3:
            self.image = self.right
        elif self.direction == 9:
            self.image = self.left

        self.checkAttack()

    def die(self):
        pass

    def getInput(self):
        self.xmove = 0
        self.ymove = 0
        keys = self.world.get_state().get_game().get_inputManager().get_keys()
        if keys[pygame.K_s]:
            self.ymove += self.speed
            self.rect.y += self.speed
        if keys[pygame.K_w]:
            self.ymove -= self.speed
            self.rect.y -= self.speed
        if keys[pygame.K_d]:
            self.xmove += self.speed
            self.rect.x += self.speed
            if not self.attacking:
                self.direction = 0
        if keys[pygame.K_a]:
            self.xmove -= self.speed
            self.rect.x -= self.speed
            if not self.attacking:
                self.direction = 1

    def checkAttack(self):
        self.attackTimer += time.perf_counter() - self.lastAttack
        self.lastAttack = time.perf_counter()
        if self.attackTimer < self.attackSpeed:
            return
        elif self.world.get_state().get_game().get_inputManager().get_pressed(0):
            self.attacking = True
            x = self.world.get_state().get_game().get_inputManager().get_x()
            y = self.world.get_state().get_game().get_inputManager().get_y()
            if x - self.rect.x > 0:
                self.direction = 0
            else:
                self.direction = 1

            self.weapon.attack(x, y)
            self.attackTimer = 0
        else:
            self.attacking = False
