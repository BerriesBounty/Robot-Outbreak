import time
from abc import ABC, abstractmethod


class Ultimate(ABC):

    def __init__(self, duration, energy):
        self.player = None
        self.name = ""
        self.description = ""
        self.cost = 0
        self.duration = duration
        self.energy = energy
        self.timer = 0
        self.lastTime = time.perf_counter()

    @abstractmethod
    def tick(self):
        pass

    def activate(self):
        pass

    def deactivate(self):
        pass
