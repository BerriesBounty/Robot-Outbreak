import random
import pygame

from entities.creatures.enemy import Enemy
from entities.creatures.player import Player


class World:
    def __init__(self, state, path):
        self.state = state
        self.width = self.height = self.spawnX = self.spawnY = None
        self.tiles = []
        # self.load_world(path)

        self.bullet_list = pygame.sprite.Group()
        self.target_list = pygame.sprite.Group()
        self.all_list = pygame.sprite.Group()

        for i in range(20):
            target = Enemy(self)
            target.setxy(random.randint(0, self.state.game.width - target.rect.width),
                         random.randint(0, self.state.game.height / 2))
            self.target_list.add(target)
            self.all_list.add(target)

        self.player = Player(self)

    def tick(self):
        self.all_list.update()

    def render(self, display):
        self.all_list.draw(display)

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
