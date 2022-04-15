from gfx import assets
from entities.creatures.creature import Creature


class Enemy(Creature):
    def __init__(self, world):
        super().__init__(world)
        self.image = assets.target
        self.rect = self.image.get_rect()
        self.health = 3

    def setxy(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.health <= 0:
            self.kill()

    def die(self):
        pass

