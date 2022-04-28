import time
import pygame
from gfx import assets
from entities.creatures.creature import Creature
from gfx.animation import Animation
from ultimates.ultManager import UltManager
from ultimates.ult_rage import Rage
from weapons.assaultRifle import AssaultRifle
from weapons.coolSword import CoolSword
from weapons.lazerBeam import PiercingGun
from weapons.pistol import Pistol
from weapons.sword import Sword


class Player(Creature):
    def __init__(self, world):
        super().__init__(world)
        self.maxHealth = 100
        self.health = self.maxHealth - 40
        self.idleRight = Animation(0.15, assets.playerIdleRight, 0)  # the animations for different actions
        self.idleLeft = Animation(0.15, assets.playerIdleLeft, 0)
        self.walkingRight = Animation(0.15, assets.playerWalkingRight, 0)
        self.walkingLeft = Animation(0.15, assets.playerWalkingLeft, 0)
        self.dying = Animation(0.15, assets.playerDeath, 1)

        self.ismoving = False  # is the player currently moving
        self.canMove = True  # does the game allow the player to take action

        self.curAnimation = self.idleRight
        self.image = self.curAnimation.getCurrentFrame()
        self.rect = self.image.get_rect()
        self.collisionRect = pygame.rect.Rect(9, 30, 16, 18)

        self.setxy()
        self.direction = 0  # direction of clock

        self.weapons = []
        self.weapons.append(PiercingGun())
        self.weapons[0].entity = self
        self.equippedWeapon = self.weapons[0]

        self.ultimate = UltManager.ultimateList[2]
        self.ultimate.player = self
        self.maxEnergy = self.ultimate.energy
        self.energy = self.ultimate.energy
        self.ultimateOn = False
        self.visible = True
        self.dead = False

        self.kills = 0

        self.world.entityManager.add(self)
    def setxy(self):
        self.rect.x = self.world.state.game.width / 2 - self.rect.width / 2
        self.rect.y = self.world.state.game.height - self.rect.height - 100

    def reset(self):
        self.ultimateOn = False
        self.ultimate.deactivate()

    def removeWeapon(self):
        if len(self.weapons) == 2:
            if self.equippedWeapon == self.weapons[0]:
                self.weapons[0] = self.weapons[1]
                self.equippedWeapon = self.weapons[0]
                self.weapons = [self.weapons[0]]
            if self.equippedWeapon == self.weapons[1]:
                self.equippedWeapon = self.weapons[0]
                self.weapons = [self.weapons[0]]
        else:
            self.weapons[0] = Sword()
            self.weapons[0].entity = self
            self.equippedWeapon = self.weapons[0]

    def update(self):
        self.idleRight.tick()
        self.idleLeft.tick()
        if self.ismoving:
            self.walkingLeft.tick()
            self.walkingRight.tick()
        else:
            self.walkingLeft.reset()
            self.walkingRight.reset()
        if self.dead:
            self.dying.tick()
        else:
            self.dying.reset()

        if self.health <= 0:
            self.die()
            self.world.gameOver = True
            self.world.endingMessage = "I'm not mad, just disappointed"

        #movement & camera
        if self.canMove:
            self.getInput()
            self.move()
            self.world.state.game.gameCamera.centerOnPlayer(self)

            #the direction the player should face
            mx = self.world.state.game.inputManager.offsetX
            if mx - self.rect.x - (self.rect.width / 2) > 0:
                self.direction = 0
            else:
                self.direction = 1

        self.image = self.getAnimationFrame()
        if self.equippedWeapon is not None:
            self.equippedWeapon.update()  # update weapon related tasks

        if self.canMove:
            #update ultimate ability
            if self.world.state.game.inputManager.keyJustPressed.get("q") and self.energy == self.maxEnergy\
                    and self.ultimate != None:
                self.ultimateOn = True
                self.ultimate.activiate()
                self.energy = 0
            if self.ultimateOn:
                self.ultimate.tick()

    def die(self):
        self.canMove = False
        self.equippedWeapon = None
        self.dead = True


    def getInput(self):
        self.xmove = 0
        self.ymove = 0
        keys = self.world.state.game.inputManager.keys
        if keys[pygame.K_s]:
            self.ymove += self.speed
        if keys[pygame.K_w]:
            self.ymove -= self.speed
        if keys[pygame.K_d]:
            self.xmove += self.speed
        if keys[pygame.K_a]:
            self.xmove -= self.speed

        if self.xmove != 0 or self.ymove != 0:
            self.ismoving = True
        else:
            self.ismoving = False

        if keys[pygame.K_1]:
            if self.equippedWeapon != self.weapons[0]:
                self.equippedWeapon = self.weapons[0]
        if keys[pygame.K_2]:
            if len(self.weapons) == 2:
                if self.equippedWeapon != self.weapons[1]:
                    self.equippedWeapon = self.weapons[1]

    def render(self, display):
        display.blit(self.image, (self.rect.x - self.world.state.game.gameCamera.xOffset,
                                                self.rect.y - self.world.state.game.gameCamera.yOffset))
        if self.equippedWeapon is not None:
            self.equippedWeapon.render(display)

    def getAnimationFrame(self):
        if self.dead:
            if self.dying.loops != 0:
                return self.dying.getCurrentFrame()
            else:
                return self.dying.frames[7]
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



