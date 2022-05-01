import time
from abc import ABC, abstractmethod


class Ultimate(ABC):

    def __init__(self, duration, energy, id):
        self.player = None
        self.name = ""
        self.description = ""
        self.cost = 0
        self.duration = duration
        self.energy = energy
        self.id = id
        self.timer = 0
        self.lastTime = time.perf_counter()

    @abstractmethod
    def tick(self):
        pass

    @abstractmethod
    def activiate(self):
        pass

    @abstractmethod
    def deactivate(self):
        pass
