import time
import pygame
from gfx import assets
from entities.creatures.creature import Creature
from gfx.animation import Animation
from weapons.assaultRifle import AssaultRifle
from weapons.pistol import Pistol
from weapons.sword import Sword


class Player(Creature):
    def __init__(self, world):
        super().__init__(world)
        self.left = assets.leftCannon
        self.right = assets.rightCannon
        self.idleRight = Animation(0.15, assets.playerIdleRight)
        self.idleLeft = Animation(0.15, assets.playerIdleLeft)
        self.walkingRight = Animation(0.15, assets.playerWalkingRight)
        self.walkingLeft = Animation(0.15, assets.playerWalkingLeft)
        self.ismoving = False

        self.curAnimation = self.idleRight
        self.image = self.curAnimation.getCurrentFrame()
        self.rect = self.image.get_rect()

        self.setxy()
        self.direction = 0  # direction of clock

        self.weapons = [None] * 2
        self.weapons[0] = Pistol(self, self.world.target_list)
        self.weapons[1] = AssaultRifle(self, self.world.target_list)
        self.equippedWeapon = self.weapons[0]

        self.world.entityManager.add(self)
        self.world.entityManager.add(self.equippedWeapon)

    def setxy(self):
        self.rect.x = self.world.state.game.width / 2 - self.rect.width / 2
        self.rect.y = self.world.state.game.height - self.rect.height

    def update(self):
        self.idleRight.tick()
        self.idleLeft.tick()
        if self.ismoving:
            self.walkingLeft.tick()
            self.walkingRight.tick()
        else:
            self.walkingLeft.index = 0
            self.walkingRight.index = 0

        self.getInput()
        self.world.state.game.gameCamera.centerOnPlayer(self)

        mx = self.world.state.game.inputManager.offsetX
        if mx - self.rect.x - (self.rect.width / 2) > 0:
            self.direction = 0
            self.curAnimation = self.idleRight
        else:
            self.direction = 1
            self.image = self.left
        self.equippedWeapon.attack()


    def die(self):
        pass

    def getInput(self):
        self.xmove = 0
        self.ymove = 0
        keys = self.world.state.game.inputManager.keys
        if keys[pygame.K_s]:
            self.ymove += self.speed
            self.rect.y += self.speed
        if keys[pygame.K_w]:
            self.ymove -= self.speed
            self.rect.y -= self.speed
        if keys[pygame.K_d]:
            self.xmove += self.speed
            self.rect.x += self.speed
        if keys[pygame.K_a]:
            self.xmove -= self.speed
            self.rect.x -= self.speed

        if self.xmove != 0 or self.ymove != 0:
            self.ismoving = True
        else:
            self.ismoving = False

        if keys[pygame.K_1]:
            if self.equippedWeapon != self.weapons[0]:
                self.world.entityManager.remove(self.equippedWeapon)
                self.equippedWeapon = self.weapons[0]
                self.world.entityManager.add(self.equippedWeapon)
        if keys[pygame.K_2]:
            if self.equippedWeapon != self.weapons[1]:
                self.world.entityManager.remove(self.equippedWeapon)
                self.equippedWeapon = self.weapons[1]
                self.world.entityManager.add(self.equippedWeapon)

    def render(self, display):
        display.blit(self.getAnimationFrame(), (self.rect.x - self.world.state.game.gameCamera.xOffset,
                                                self.rect.y - self.world.state.game.gameCamera.yOffset))

    def getAnimationFrame(self):
        if not self.ismoving:
            if self.direction == 0:
                return self.idleRight.getCurrentFrame()
            else:
                return self.idleLeft.getCurrentFrame()
        else:
            if self.direction == 0:
                return self.walkingRight.getCurrentFrame()
            else:
                return self.walkingLeft.getCurrentFrame()


