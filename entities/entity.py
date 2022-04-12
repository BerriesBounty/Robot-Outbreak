from abc import ABC, abstractmethod

import pygame.sprite


class Entity(ABC, pygame.sprite.Sprite):
    DEFAULT_HEALTH = 100

    def __init__(self, world):
        super().__init__()
        self.world = world
        self.health = Entity.DEFAULT_HEALTH
        self.isActive = True
        self.image = None
        self.rect = None

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def die(self):
        pass
