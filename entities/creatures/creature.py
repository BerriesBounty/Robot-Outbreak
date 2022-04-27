from abc import ABC

from entities.entity import Entity
from gfx.tiles import Tile


class Creature(Entity, ABC):
    DEFAULT_SPEED = 6.0

    def __init__(self, world):
        super().__init__(world)
        self.speed = Creature.DEFAULT_SPEED
        self.ymove = 0
        self.xmove = 0

    def move(self):
        if not self.checkCollision(self.xmove, 0):
            self.moveX()
        if not self.checkCollision(0, self.ymove):
            self.moveY()

    def moveX(self):
        if self.xmove > 0:
            dx = int(self.rect.x + self.xmove + self.collisionrect.x + self.collisionrect.width) // Tile.WIDTH
            dy = int(self.rect.y + self.collisionrect.y) // Tile.HEIGHT
            if not self.world.getTile(dx, dy).isSolid and not self.world.getTile(dx
                    , dy + self.collisionrect.height // Tile.HEIGHT).isSolid:
                self.rect.x += self.xmove
            else:
                self.rect.x = dx * Tile.WIDTH - self.collisionrect.x - self.collisionrect.width - 1
        elif self.xmove < 0:
            dx = int(self.rect.x + self.xmove + self.collisionrect.x) // Tile.WIDTH
            dy = int(self.rect.y + self.collisionrect.y) // Tile.HEIGHT
            if not self.world.getTile(dx, dy).isSolid and not self.world.getTile(dx
                , dy + self.collisionrect.height // Tile.HEIGHT).isSolid:
                self.rect.x += self.xmove
            else:
                self.rect.x = dx * Tile.WIDTH + Tile.WIDTH - self.collisionrect.x

    def moveY(self):
        if self.ymove > 0:
            dy = int(self.rect.y + self.ymove + self.collisionrect.y + self.collisionrect.height) // Tile.HEIGHT
            dx = int(self.rect.x + self.collisionrect.x) // Tile.WIDTH
            if not self.world.getTile(dx, dy).isSolid and not self.world.getTile(dx + self.collisionrect.width //
                                                                                 Tile.WIDTH, dy).isSolid:
                self.rect.y += self.ymove
            else:
                self.rect.y = dy * Tile.HEIGHT - self.collisionrect.y - self.collisionrect.height - 1
        elif self.ymove < 0:
            dy = int(self.rect.y + self.ymove + self.collisionrect.y) // Tile.HEIGHT
            dx = int(self.rect.x + self.collisionrect.x) // Tile.WIDTH
            if not self.world.getTile(dx, dy).isSolid and not self.world.getTile(dx + self.collisionrect.width //
                                                                                 Tile.WIDTH, dy).isSolid:
                self.rect.y += self.ymove
            else:
                self.rect.y = dy * Tile.HEIGHT + Tile.HEIGHT - self.collisionrect.y
