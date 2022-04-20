import pygame.sprite


class EntityManager(pygame.sprite.Group):  # a child class of groups
    def __init__(self):
        super().__init__()

    def draw(self, surface):  # change the draw function so that each entity chose how to be drawn
        for i in self.sprites():
            i.render(surface)  # call the render function of all the sprites
