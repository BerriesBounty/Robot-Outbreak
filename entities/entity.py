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

    @abstractmethod
    def render(self, display):
        pass

    def hurt(self, n):
        self.health -= n

    def checkCollision(self, dx, dy):
        collisionRect = pygame.rect.Rect(self.rect.x + dx, self.rect.y + dy, self.rect.width, self.rect.height)
        for e in self.world.entityManager:
            if e == self:
                continue
            elif collisionRect.colliderect(e.rect):
                return True
        return False

