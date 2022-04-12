from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, game):
        self.game = game

    @abstractmethod
    def tick(self):
        pass

    @abstractmethod
    def render(self, display):
        pass


class StateManager:
    def __init__(self):
        self.currentState = None

    def set_state(self, state):
        self.currentState = state

    def get_state(self):
        return self.currentState
