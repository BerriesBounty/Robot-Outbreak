import pygame.sprite


class EntityManager(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def draw(self, surface):
        for i in self.sprites():
            i.render(surface)
