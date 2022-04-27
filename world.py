import random
import pygame

from entities.creatures.rangedEnemy import RangedEnemy
from entities.creatures.player import Player
from entities.entityManager import EntityManager
from gfx.tiles import Tile
from timer import Timer
from ui.hudManager import HUDManager
from ui.itemShop import ItemShop


class World:
    def __init__(self, state):
        self.state = state  # the state the world is in
        self.width = self.height = self.spawnX = self.spawnY = None
        self.tiles = []
        self.mapImg = pygame.image.load("res/map.png")
        self.loadMap()

        self.entityManager = EntityManager()  # store all the entities, including enemies and player
        self.player = Player(self)  # create the player

        self.bullet_list = EntityManager()  # store all the bullets in the world
        self.target_list = pygame.sprite.Group()  # store all the enemies in the world

        self.wave = 1
        self.waveStart()

        self.player.enemies = self.target_list
        self.hud = HUDManager(self)  # create the heads-up display
        self.itemShop = None
        self.stage = 1
        self.timer = None

    def tick(self):
        # update all the entities and the HUD
        if self.stage % 2 == 1:
            self.bullet_list.update()
            self.entityManager.update()
            self.hud.tick()
            if self.timer is not None and self.timer.update():
                self.stage += 1
        else:
            if self.timer.update():
                self.itemShop.tick()

    def render(self, display):
        xStart = int(max(0, self.state.game.gameCamera.xOffset // Tile.WIDTH))
        yStart = int(max(0, self.state.game.gameCamera.yOffset // Tile.HEIGHT))
        xEnd = int(min(self.mapImg.get_width(),
                   (self.state.game.gameCamera.xOffset + self.state.game.width) // Tile.WIDTH) + 1)
        yEnd = int(min(self.mapImg.get_height(),
                   (self.state.game.gameCamera.yOffset + self.state.game.height) // Tile.HEIGHT) + 1)
        for y in range(yStart, yEnd):
            for x in range(xStart, xEnd):
                if self.getTile(x, y).image is not None:
                    display.blit(self.getTile(x, y).image, (int(x * Tile.WIDTH - self.state.game.gameCamera.xOffset),
                             int(y * Tile.HEIGHT - self.state.game.gameCamera.yOffset)))

        if self.stage % 2 == 1:
            self.bullet_list.draw(display)
            self.entityManager.draw(display)
            self.hud.render(display)
        else:
            self.itemShop.render(display)

    def waveCleared(self):
        self.player.ismoving = False
        self.player.canMove = False
        self.itemShop = ItemShop(self)
        self.timer = Timer(2)
        self.player.reset()

    def waveStart(self):
        x = random.randint(1,5)
        y = random.randint(1,3)
        self.wave += 1
        x = x + self.wave%3*2
        for i in range(x):
            target = RangedEnemy(self, "easy")
            while True:
                posX = random.randint(0, self.mapImg.get_width())
                posY = random.randint(0, self.mapImg.get_height())
                if self.getTile(posX,posY).color != (0, 1, 0, 255) and not self.getTile(posX, posY).isSolid:
                    break
            target.setxy(posX * Tile.WIDTH, posY * Tile.HEIGHT)
            self.target_list.add(target)
            self.entityManager.add(target)
        # for i in range(y):
        #     target = MeleeEnemy(self, 3)
        #     while True:
        #         posX = random.randint(0, self.mapImg.get_width())
        #         posY = random.randint(0, self.mapImg.get_height())
        #         if self.getTile(posX, posY).color != (0, 1, 0, 255) and not self.getTile(posX, posY).isSolid:
        #             break
        #     target.setxy(posX * Tile.WIDTH, posY * Tile.HEIGHT)
        #     self.target_list.add(target)
        #     self.entityManager.add(target)

    def loadMap(self):
        print(self.mapImg.get_width(), self.mapImg.get_height())
        for x in range(self.mapImg.get_width()):
            row = []
            for y in range(self.mapImg.get_height()):
                tile = Tile(self.mapImg.get_at((x, y)))
                row.append(tile)
            self.tiles.append(row)

    def getTile(self, x, y):
        if x < 0 or y < 0 or x >= self.mapImg.get_width() or y >= self.mapImg.get_height():
            return self.tiles[0][0]
        return self.tiles[x][y]
