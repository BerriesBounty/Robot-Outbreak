from abc import ABC, abstractmethod


class State(ABC):  # abstract class
    def __init__(self, game):  # takes in the game class the state is running in
        self.game = game

    # abstract methods are passed down to all its child classes
    @abstractmethod
    def tick(self):
        pass

    @abstractmethod
    def render(self, display):
        pass


# manages which state the game is currently in
class StateManager:
    def __init__(self):
        self.currentState = None

    def set_state(self, state):
        self.currentState = state

    def get_state(self):
        return self.currentState
