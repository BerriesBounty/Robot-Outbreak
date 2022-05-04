import pygame
from gfx import assets
from entities.creatures.creature import Creature
from gfx.animation import Animation
from weapons.sword import Sword


class Player(Creature):
    def __init__(self, world):
        super().__init__(world)
        self.money = 100
        self.maxHealth = 100
        self.health = self.maxHealth

        # the animations for different actions
        self.idleRight = Animation(0.15, assets.playerIdleRight, 0)
        self.idleLeft = Animation(0.15, assets.playerIdleLeft, 0)
        self.walkingRight = Animation(0.15, assets.playerWalkingRight, 0)
        self.walkingLeft = Animation(0.15, assets.playerWalkingLeft, 0)
        self.dying = Animation(0.15, assets.playerDeath, 1)

        self.isMoving = False  # is the player currently moving
        self.canMove = True  # does the game allow the player to take action

        self.curAnimation = self.idleRight
        self.image = self.curAnimation.getCurrentFrame()
        self.rect = self.image.get_rect()
        self.collisionRect = pygame.rect.Rect(9, 30, 16, 18)  # the rectangle that collides with walls

        self.setxy()
        self.direction = 0  # direction of clock

        self.weapons = []  # player can hold two weapons
        self.weapons.append(Sword())  # starting weapon
        self.weapons[0].entity = self
        self.equippedWeapon = self.weapons[0]  # which weapon the player is currently using

        self.ultimate = None
        self.maxEnergy = 100
        self.energy = 100
        self.ultimateOn = False
        self.dead = False

        self.kills = 0  # amount of kills

        self.world.entityManager.add(self)

    def setxy(self):  # set player in the middle of the screen
        self.rect.x = self.world.state.game.width / 2 - self.rect.width / 2
        self.rect.y = self.world.state.game.height - self.rect.height - 100

    def reset(self):  # when a wave is cleared, stop the ultimate ability
        self.ultimateOn = False
        self.ultimate.deactivate()

    def removeWeapon(self):
        if len(self.weapons) == 2:  # if the player has another weapon to use
            if self.equippedWeapon == self.weapons[0]:  # if equipped weapon is first weapon
                self.weapons[0] = self.weapons[1]
                self.equippedWeapon = self.weapons[0]  # make the player equipped the other weapon
                self.weapons = [self.weapons[0]]
            if self.equippedWeapon == self.weapons[1]:
                self.equippedWeapon = self.weapons[0]
                self.weapons = [self.weapons[0]]
        else:
            self.weapons[0] = Sword()  # replace current weapon with sword
            self.weapons[0].entity = self
            self.equippedWeapon = self.weapons[0]

    def update(self):
        # tick the animations to update the frame of it
        self.idleRight.tick()
        self.idleLeft.tick()
        if self.isMoving:
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

        # movement & camera
        if self.canMove:
            self.getInput()  # get the keyboard inputs
            self.move()
            self.world.state.game.gameCamera.centerOnPlayer(self)  # center the camera

            # the direction the player should face
            mx = self.world.state.game.inputManager.offsetX
            if mx - self.rect.x - (self.rect.width / 2) > 0:
                self.direction = 0
            else:
                self.direction = 1

        self.image = self.getAnimationFrame()  # update the image
        if self.equippedWeapon is not None:
            self.equippedWeapon.update()  # update weapon related tasks

        if self.canMove:
            # update ultimate ability
            if self.world.state.game.inputManager.keyJustPressed.get("q") and self.energy == self.maxEnergy \
                    and self.ultimate is not None:  # if the player can use ultimate
                self.ultimateOn = True
                self.ultimate.activate()
                self.energy = 0
            if self.ultimateOn:
                self.ultimate.tick()

    def die(self):
        self.canMove = False
        self.equippedWeapon = None  # do not display weapon
        self.dead = True

    def getInput(self):
        self.xmove = 0  # how much the player moves horizontally
        self.ymove = 0  # how much the player moves vertically
        keys = self.world.state.game.inputManager.keys
        if keys[pygame.K_s]:
            self.ymove += self.speed  # add the amount to move per frame to ymove
        if keys[pygame.K_w]:
            self.ymove -= self.speed
        if keys[pygame.K_d]:
            self.xmove += self.speed
        if keys[pygame.K_a]:
            self.xmove -= self.speed

        # if the player is moving or not
        if self.xmove != 0 or self.ymove != 0:
            self.isMoving = True
        else:
            self.isMoving = False

        # switching between weapons
        if keys[pygame.K_1]:
            if self.equippedWeapon != self.weapons[0]:
                self.equippedWeapon = self.weapons[0]
        if keys[pygame.K_2]:
            if len(self.weapons) == 2:  # does the player have more than 1 weapon
                if self.equippedWeapon != self.weapons[1]:
                    self.equippedWeapon = self.weapons[1]

    def render(self, display):  # draw the player and the weapon
        display.blit(self.image, (self.rect.x - self.world.state.game.gameCamera.xOffset,
                                  self.rect.y - self.world.state.game.gameCamera.yOffset))
        if self.equippedWeapon is not None:
            self.equippedWeapon.render(display)

    def getAnimationFrame(self):  # which image from which animation to take
        if self.dead:
            if self.dying.loops != 0:  # if the animation finished its loop
                return self.dying.getCurrentFrame()  # display the last image of the animation
            else:
                return self.dying.frames[7]
        if not self.isMoving:
            if self.direction == 0:
                return self.idleRight.getCurrentFrame()
            else:
                return self.idleLeft.getCurrentFrame()
        else:
            if self.direction == 0:
                return self.walkingRight.getCurrentFrame()
            else:
                return self.walkingLeft.getCurrentFrame()
