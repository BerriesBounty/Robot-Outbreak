from entities.creatures.creature import Creature
from gfx import assets
from gfx.animation import Animation


# the image created from invisibility ultimate
class Decoy(Creature):
    def __init__(self, world, x, y):
        super().__init__(world)
        self.dead = False
        self.collide = False  # the sprite is not able to be hit
        self.dying = Animation(0.15, assets.playerDeath, 1)
        self.image = self.dying.getCurrentFrame()  # won't be displayed
        self.rect = self.image.get_rect()
        self.rect.x = x  # set the position to where the player casted the ultimate
        self.rect.y = y

        for i in self.world.target_list:  # change all the enemies to target the decoy instead of the player
            i.enemies = [self]

    def update(self):
        # if the ultimate has ended, display death animation
        if self.dead:
            self.dying.tick()
            if self.dying.loops == 0:  # once the death animation finishes, kill the decoy
                self.kill()
        else:
            self.dying.reset()

    def die(self):
        for i in self.world.target_list:  # reset who the enemy target
            i.enemies = [self.world.player]
        self.dead = True

    def render(self, display):
        if not self.dead:  # display the player's current animation
            display.blit(self.world.player.getAnimationFrame(), (self.rect.x - self.world.state.game.gameCamera.xOffset,
                                                                 self.rect.y - self.world.state.game.gameCamera.yOffset))
        else:
            display.blit(self.dying.getCurrentFrame(), (self.rect.x - self.world.state.game.gameCamera.xOffset,
                                                        self.rect.y - self.world.state.game.gameCamera.yOffset))
        pass
