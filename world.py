import random
import pygame

from entities.creatures.rangedEnemy import RangedEnemy
from entities.creatures.meleeEnemy import MeleeEnemy
from entities.creatures.boss import FinalBoss
from entities.creatures.player import Player
from entities.entityManager import EntityManager
from gfx import assets
from gfx.tiles import Tile
from timer import Timer
from ui.hudManager import HUDManager
from ui.itemShop import ItemShop


class World:
    def __init__(self, state):
        self.state = state  # the state the world is in
        self.width = self.height = self.spawnX = self.spawnY = None
        self.tiles = []  # the map and what tile is corresponding to what position
        self.mapImg = pygame.image.load("res/map.png")  # color code of the map
        self.loadMap()

        self.entityManager = EntityManager()  # store all the entities, including enemies and player
        self.player = Player(self)  # create the player

        self.bullet_list = EntityManager()  # store all the bullets in the world
        self.target_list = pygame.sprite.Group()  # store all the enemies in the world
        self.resource_list = EntityManager()  # store all the resource drops
        self.wave = 0
        self.finalWave = 10
        self.boss = None
        self.waveStart()

        self.player.enemies = self.target_list  # make all the enemies the player's enemies
        self.hud = HUDManager(self)  # create the heads-up display
        self.itemShop = None
        self.stage = 1  # every odd stage is a wave and every even stage is an item shop
        self.timer = None  # delay between waves and item shop
        self.gameOver = False
        self.endingMessage = ""
        self.endBox = pygame.surface.Surface((175, 50))  # the restart button
        self.endBox.fill((136, 206, 242))
        self.endBox.set_alpha(25)
        self.endRect = self.endBox.get_rect(center=(self.state.game.width / 2, self.state.game.height / 2 + 100))

    def tick(self):
        # update all the entities and the HUD
        if self.stage % 2 == 1:
            self.bullet_list.update()
            self.entityManager.update()
            self.resource_list.update()
            self.hud.tick()
            if self.timer is not None and self.timer.update():  # if the timer has started and has finished
                self.stage += 1  # move on to item shop
                self.player.isMoving = False  # make the player display idle animation
                self.player.canMove = False  # make the player not able to do anything
        else:  # item shop stage
            self.itemShop.tick()
        if self.gameOver:  # if player died

            # if hovering restart
            if self.endRect.collidepoint(self.state.game.inputManager.x, self.state.game.inputManager.y):
                self.endBox.set_alpha(50)
                if self.state.game.inputManager.mouseJustReleased[0]:  # if clicked
                    self.state.restart()
            else:
                self.endBox.set_alpha(25)

    def render(self, display):
        # what part of the map to start and stop rendering
        xStart = int(max(0, self.state.game.gameCamera.xOffset // Tile.WIDTH))  # get the tile index
        yStart = int(max(0, self.state.game.gameCamera.yOffset // Tile.HEIGHT))
        xEnd = int(min(self.mapImg.get_width(),
                       (self.state.game.gameCamera.xOffset + self.state.game.width) // Tile.WIDTH) + 1)
        yEnd = int(min(self.mapImg.get_height(),
                       (self.state.game.gameCamera.yOffset + self.state.game.height) // Tile.HEIGHT) + 1)

        # draw the map
        for y in range(yStart, yEnd):
            for x in range(xStart, xEnd):
                if self.getTile(x, y).image is not None:  # if there is something to draw
                    # draw the tile at the position
                    display.blit(self.getTile(x, y).image, (int(x * Tile.WIDTH - self.state.game.gameCamera.xOffset),
                                                            int(y * Tile.HEIGHT - self.state.game.gameCamera.yOffset)))

        # draw all other stuff
        if self.stage % 2 == 1:
            self.bullet_list.draw(display)
            self.entityManager.draw(display)
            self.resource_list.draw(display)
            self.hud.render(display)
        else:
            self.itemShop.render(display)

        if self.wave == self.finalWave:
            pygame.draw.rect(display, assets.bgWhite, (100, 550, 600, 20))
            pygame.draw.rect(display, (200, 0, 0), (100, 550, (self.boss.health / self.boss.maxHealth) * 600, 20))

        # draw game over message and restart button
        if self.gameOver:
            assets.renderFont(display, self.endingMessage, (186, 200, 216), (32, 51, 67), self.state.game.width / 2,
                              150, assets.fonts[2])
            display.blit(self.endBox, self.endRect)
            assets.renderFont(display, "Restart", (186, 200, 216), (32, 51, 67), self.state.game.width / 2,
                              self.state.game.height / 2 + 100, assets.fonts[2])


    def waveCleared(self):
        if self.wave == self.finalWave:
            self.gameOver = True
            self.endingMessage = "You win! Now do it again."
        else:
            assets.backgroundSound[1].play()  # play wave clear sound effect
            self.itemShop = ItemShop(self)
            self.timer = Timer(2)  # set up a delay between wave and item shop
            if self.player.ultimateOn:
                self.player.reset()  # deactivate ultimate

    def waveStart(self):
        # choose a random amount of enemies
        self.wave += 1
        if self.wave == self.finalWave:
            assets.bossSound[0].play()
            self.boss = FinalBoss(self)
            while True:
                posX = random.randint(0, self.mapImg.get_width())
                posY = random.randint(0, self.mapImg.get_height())
                if self.getTile(posX, posY).color != (0, 1, 0, 255) and not self.getTile(posX, posY).isSolid:
                    break
            self.boss.setxy(posX * Tile.WIDTH, posY * Tile.HEIGHT)
            self.target_list.add(self.boss)
            self.entityManager.add(self.boss)
        else:
            if self.wave == 1:
                x = 2
                y = 2
            else:
                x = random.randint(2, 5)
                y = random.randint(1, 3)
            x = x + self.wave // 2
            # ranged enemy
            for i in range(x):
                target = RangedEnemy(self, "easy")
                while True:
                    posX = random.randint(0, self.mapImg.get_width())  # place enemy at a random position
                    posY = random.randint(0, self.mapImg.get_height())

                    # if the tile is not blank and not solid
                    if self.getTile(posX, posY).color != (0, 1, 0, 255) and not self.getTile(posX, posY).isSolid:
                        break
                target.setxy(posX * Tile.WIDTH, posY * Tile.HEIGHT)
                self.target_list.add(target)
                self.entityManager.add(target)
            for i in range(y):
                target = MeleeEnemy(self, "easy")
                while True:
                    posX = random.randint(0, self.mapImg.get_width())
                    posY = random.randint(0, self.mapImg.get_height())
                    if self.getTile(posX, posY).color != (0, 1, 0, 255) and not self.getTile(posX, posY).isSolid:
                        break
                target.setxy(posX * Tile.WIDTH, posY * Tile.HEIGHT)
                self.target_list.add(target)
                self.entityManager.add(target)


    def loadMap(self):
        # load each individual pixel of the map
        for x in range(self.mapImg.get_width()):
            row = []
            for y in range(self.mapImg.get_height()):
                tile = Tile(self.mapImg.get_at((x, y)))
                row.append(tile)
            self.tiles.append(row)

    def getTile(self, x, y):  # return the tile in the tile list
        if x < 0 or y < 0 or x >= self.mapImg.get_width() or y >= self.mapImg.get_height():
            return self.tiles[0][0]
        return self.tiles[x][y]
