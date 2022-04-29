from gfx import assets
from entities.creatures.creature import Creature
import random
from entities.resources.healthpot import HealthDrop
from weapons.enemySword import EnemySword
from timer import Timer

class MeleeEnemy(Creature):
    def __init__(self, world, difficulty):
        super().__init__(world)
        self.image = assets.target
        self.rect = self.image.get_rect()
        self.difficulty = difficulty
        self.health = 0
        self.checkdiff()
        self.animation_count = 0
        self.reset_offset = 0
        self.offset_x = random.randrange(-150, 150)
        self.offset_y = random.randrange(-150, 150) #the goal of the enemy is to attack the player and as such it will move towards the player, to add variety we have added the offset value so that for example if the player is at 0,0 -> the offset will cause the enemy to move towards a random point in that range - we will reset the offset randomly to offer that variability.
        self.timer = Timer(random.randint(1, 7))
        self.weapon = EnemySword()
        self.weapon.entity = self
        self.direction = 0
        self.enemies = [self.world.player]


    def checkdiff(self):
        if self.difficulty == "easy":
            self.health = 3
        elif self.difficulty == "medium":
            self.health = 5
        elif self.difficulty == "hard":
            self.health = 7
    def setxy(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.world.player.rect.x - self.rect.x == 50:
            self.weapon.attack()

        reset_offset = random.randint(0,20)
        if reset_offset == 15:
            self.offset_x = random.randrange(-150, 150)
            self.offset_y = random.randrange(-150, 150)

        if self.health <= 0:
            resource = random.randint(1, 100)
            if resource == range(1, 25):
                HealthDrop(self.rect.x,self.rect.y)
                HealthDrop.main()
            elif resource == range(25, 50):
                pass
            elif resource == range(51, 75):
                pass
            else:
                pass

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
        display.blit(self.image, (self.rect.x - self.world.state.game.gameCamera.xOffset,
                                  self.rect.y - self.world.state.game.gameCamera.yOffset))
        self.weapon.render(display)

    def die(self):

        pass



