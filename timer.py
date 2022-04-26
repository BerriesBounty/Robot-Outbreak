import time


class Timer:
    def __init__(self, goal):
        self.timer = 0
        self.lastTime = time.perf_counter()
        self.goal = goal

    def update(self):
        self.timer += time.perf_counter() - self.lastTime
        self.lastTime = time.perf_counter()
        if self.timer > self.goal:
            return True
        else:
            return False

    def reset(self):
        self.timer = 0