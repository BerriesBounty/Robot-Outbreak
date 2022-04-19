import random
import pygame

from entities.creatures.enemy import Enemy
from entities.creatures.player import Player
from entities.entityManager import EntityManager
from ui.hudManager import HUDManager
from ui.itemShop import ItemShop


class World:
    def __init__(self, state, path):
        self.state = state  # the state the world is in
        self.width = self.height = self.spawnX = self.spawnY = None
        self.tiles = []
        # self.load_world(path)

        self.bullet_list = EntityManager()  # store all the bullets in the world
        self.target_list = pygame.sprite.Group()  # store all the enemies in the world
        self.entityManager = EntityManager()  # store all the entities, including enemies and player

        for i in range(5):
            target = Enemy(self)
            target.setxy(random.randint(0, self.state.game.width - target.rect.width),
                         random.randint(0, self.state.game.height / 2))
            self.target_list.add(target)
            self.entityManager.add(target)

        self.player = Player(self)  # create the player
        self.hud = HUDManager(self)  # create the heads-up display
        self.itemShop = None
        self.stage = 1

    def tick(self):
        # update all the entities and the HUD
        if self.stage % 2 == 1:
            self.bullet_list.update()
            self.entityManager.update()
            self.hud.tick()
        else:
            self.itemShop.tick()

    def render(self, display):
        if self.itemShop is None:
            self.bullet_list.draw(display)
            self.entityManager.draw(display)
            self.hud.render(display)
        else:
            self.itemShop.render(display)

    def waveCleared(self):
        self.stage += 1
        self.itemShop = ItemShop(self)

    def load_world(self, path):
        with open(path) as file:
            content = file.read().split()
        self.width = int(content[0])
        self.height = int(content[1])
        self.spawnX = int(content[2])
        self.spawnY = int(content[3])

        for x in range(self.width):
            self.tiles.append([])
            for y in range(self.height):
                self.tiles[x].append(int(content[(x * self.height + y) + 4]))
