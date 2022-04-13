import time
import pygame
import assets
from entities.creatures.creature import Creature
from weapons.assultRifle import AssultRifle
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
        self.direction = 12  # direction of clock

        self.weapon = Sword(self, self.world.target_list)
        self.attackSpeed = self.weapon.get_attackSpeed()
        self.lastAttack = time.perf_counter()
        self.attackTimer = self.attackSpeed

        self.world.all_list.add(self)
        self.world.all_list.add(self.weapon)

    def setxy(self):
        self.rect.x = self.world.game.width / 2 - self.rect.width / 2
        self.rect.y = self.world.game.height - self.rect.height

    def update(self):
        self.getInput()
        if self.direction == 3:
            self.image = self.right
        elif self.direction == 9:
            self.image = self.left
        else:
            self.image = self.center

        self.checkAttack()

    def die(self):
        pass

    def getInput(self):
        self.xmove = 0
        self.ymove = 0
        keys = self.world.game.get_inputManager().get_keys()
        if keys[pygame.K_s]:
            self.ymove += self.speed
            self.direction = 12
            self.rect.y += self.speed
        if keys[pygame.K_w]:
            self.ymove -= self.speed
            self.direction = 12
            self.rect.y -= self.speed
        if keys[pygame.K_d]:
            self.xmove += self.speed
            self.direction = 3
            self.rect.x += self.speed
        if keys[pygame.K_a]:
            self.xmove -= self.speed
            self.direction = 9
            self.rect.x -= self.speed

    def checkAttack(self):
        self.attackTimer += time.perf_counter() - self.lastAttack
        self.lastAttack = time.perf_counter()
        if self.attackTimer < self.attackSpeed:
            return
        elif self.world.game.get_inputManager().get_pressed(0):
            self.weapon.attack()
            self.attackTimer = 0