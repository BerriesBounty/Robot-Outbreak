import world
from states.state import State
from weapons.weaponManager import WeaponManager


class GameState(State):
    def __init__(self, game):
        super().__init__(game)
        WeaponManager.init()
        self.world1 = world.World(self)  # store a world that runs a level of the game

    def tick(self):
        self.world1.tick()  # tick the current level

    def render(self, display):
        self.world1.render(display)  # render the current level

    def start(self): # reset the enemies attack timer so they don't attack right as the game starts
        for i in self.world1.target_list:
            i.timer.reset()

    def restart(self):
        self.world1 = world.World(self)

