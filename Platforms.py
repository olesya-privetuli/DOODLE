import pygame
from constans import platf_width, pl_heigh, land_w, land_h


class Platforms(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.coor = self.x, self.y = (0, 0)

    def get_widt(self):
        return platf_width

    def get_heigh(self):
        return pl_heigh


class Land(Platforms):
    def __init__(self):
        super().__init__()
        self.coor = self.x, self.y = 0, 550

    def get_widt(self):
        return land_w

    def get_heigh(self):
        return land_h