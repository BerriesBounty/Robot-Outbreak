from entities.creatures.creature import Creature
from gfx import assets
from gfx.animation import Animation


class Decoy(Creature):
    def __init__(self, world, x, y):
        super().__init__(world)
        self.dead = False
        self.collide = False
        self.dying = Animation(0.15, assets.playerDeath, 1)
        self.image = self.dying.getCurrentFrame()  # won't be displayed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        for i in self.world.target_list:
            i.enemies = [self]

    def update(self):
        if self.dead:
            self.dying.tick()
            if self.dying.loops == 0:
                self.kill()
        else:
            self.dying.reset()

    def die(self):
        for i in self.world.target_list:
            i.enemies = [self.world.player]
        self.dead = True

    def render(self, display):
        if not self.dead:
            display.blit(self.world.player.getAnimationFrame(), (self.rect.x - self.world.state.game.gameCamera.xOffset,
                                                                 self.rect.y - self.world.state.game.gameCamera.yOffset))
        else:
            display.blit(self.dying.getCurrentFrame(), (self.rect.x - self.world.state.game.gameCamera.xOffset,
                                                        self.rect.y - self.world.state.game.gameCamera.yOffset))
        pass
