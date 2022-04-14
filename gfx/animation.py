import time


class Animation:
    def __init__(self, speed, frames):
        self.speed = speed
        self.frames = frames
        self.index = 0
        self.timer = 0
        self.lastTime = time.perf_counter()

    def tick(self):
        self.timer += time.perf_counter() - self.lastTime
        self.lastTime = time.perf_counter()

        if self.timer > self.speed:
            self.index += 1
            self.timer = 0
            if self.index >= len(self.frames):
                self.index = 0

    def getCurrentFrame(self):
        return self.frames[self.index]
