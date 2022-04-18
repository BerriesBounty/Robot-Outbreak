import time
from abc import ABC, abstractmethod


class Ultimate(ABC):
    def __init__(self, gamestate, duration, energy):
        self.duration = duration
        self.energy = energy
        self.gamestate = gamestate
        self.timer = 0
        self.lastTime = time.perf_counter()

    @abstractmethod
    def tick(self):
        pass