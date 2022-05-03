from abc import ABC

from entities.entity import Entity
from gfx.tiles import Tile


class Creature(Entity, ABC):
    DEFAULT_SPEED = 6.0

    def __init__(self, world):
        super().__init__(world)
        self.speed = Creature.DEFAULT_SPEED
        self.ymove = 0  # how much the creature is moving
        self.xmove = 0

    def move(self):
        if not self.checkCollision(self.xmove, 0):  # if it collides with any entities
            self.moveX()
        if not self.checkCollision(0, self.ymove):
            self.moveY()

    def moveX(self):
        if self.xmove > 0:  # if moving right
            # position of creature relative to the tiles
            dx = int(self.rect.x + self.xmove + self.collisionRect.x + self.collisionRect.width) // Tile.WIDTH
            dy = int(self.rect.y + self.collisionRect.y) // Tile.HEIGHT

            # if it does not collide with walls
            if not self.world.getTile(dx, dy).isSolid and not self.world.getTile(dx,
                                                                                 dy + self.collisionRect.height //
                                                                                 Tile.HEIGHT).isSolid:
                self.rect.x += self.xmove
            else:  # put it to the left of the tile
                self.rect.x = dx * Tile.WIDTH - self.collisionRect.x - self.collisionRect.width - 1
        elif self.xmove < 0:  # if moving left
            dx = int(self.rect.x + self.xmove + self.collisionRect.x) // Tile.WIDTH
            dy = int(self.rect.y + self.collisionRect.y) // Tile.HEIGHT
            if not self.world.getTile(dx, dy).isSolid and not self.world.getTile(dx,
                                                                                 dy + self.collisionRect.height //
                                                                                 Tile.HEIGHT).isSolid:
                self.rect.x += self.xmove
            else:
                self.rect.x = dx * Tile.WIDTH + Tile.WIDTH - self.collisionRect.x  # put it right of tile

    def moveY(self):  # same logic
        if self.ymove > 0:
            dy = int(self.rect.y + self.ymove + self.collisionRect.y + self.collisionRect.height) // Tile.HEIGHT
            dx = int(self.rect.x + self.collisionRect.x) // Tile.WIDTH
            if not self.world.getTile(dx, dy).isSolid and not self.world.getTile(dx + self.collisionRect.width //
                                                                                 Tile.WIDTH, dy).isSolid:
                self.rect.y += self.ymove
            else:
                self.rect.y = dy * Tile.HEIGHT - self.collisionRect.y - self.collisionRect.height - 1
        elif self.ymove < 0:
            dy = int(self.rect.y + self.ymove + self.collisionRect.y) // Tile.HEIGHT
            dx = int(self.rect.x + self.collisionRect.x) // Tile.WIDTH
            if not self.world.getTile(dx, dy).isSolid and not self.world.getTile(dx + self.collisionRect.width //
                                                                                 Tile.WIDTH, dy).isSolid:
                self.rect.y += self.ymove
            else:
                self.rect.y = dy * Tile.HEIGHT + Tile.HEIGHT - self.collisionRect.y
