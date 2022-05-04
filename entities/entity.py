from abc import ABC, abstractmethod

import pygame.sprite


class Entity(ABC, pygame.sprite.Sprite):  # all entities are sprites
    DEFAULT_HEALTH = 100

    def __init__(self, world):  # take in the world/level they are in
        super().__init__()  # initialize sprites
        self.world = world
        self.health = Entity.DEFAULT_HEALTH  # the health of the entity
        self.isActive = True
        self.image = None  # the image of the entity
        self.rect = None  # the size of the image
        self.collide = True  # is the entity collidable or not
        self.collisionRect = pygame.rect.Rect(9, 30, 16, 18)  # part of the image that crashes into wall

    @abstractmethod
    def update(self):  # update the entity
        pass

    @abstractmethod
    def die(self):  # when the entity dies
        pass

    @abstractmethod
    def render(self, display):  # draw the entity on display
        pass

    def hurt(self, n):  # damage the entity
        self.health -= n

    def checkCollision(self, dx, dy):  # check if the entity is colliding with any other entities if it moves

        # create the rect that the entity would be in  if it moves dx amount and dy amount
        collisionRect = pygame.rect.Rect(self.rect.x + dx, self.rect.y + dy, self.rect.width, self.rect.height)
        for e in self.world.entityManager:  # loop through all the entities
            if e == self or not e.collide:  # if the entity is itself, don't check for collision
                continue
            elif collisionRect.colliderect(e.rect):  # if the entities collide
                return True
        return False

