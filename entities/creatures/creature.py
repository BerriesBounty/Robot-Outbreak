from abc import ABC

from entities.entity import Entity


class Creature(Entity, ABC):
    DEFAULT_SPEED = 2.0

    def __init__(self, world):
        super().__init__(world)
        self.speed = Creature.DEFAULT_SPEED
        self.ymove = 0
        self.xmove = 0

    def move(self):
        if not self.checkCollision(self.xmove, 0):
            self.rect.x += self.xmove
        if not self.checkCollision(0, self.ymove):
            self.rect.y += self.ymove
