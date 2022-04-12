from abc import ABC

from entities.entity import Entity


class Creature(Entity, ABC):
    DEFAULT_SPEED = 2.0

    def __init__(self, world):
        super().__init__(world)
        self.speed = Creature.DEFAULT_SPEED
        self.ymove = self.xmove = 0

    def move(self):
        pass
