from random import randint
import pygame
from constans import platf_koords


class Platforms(pygame.sprite.Sprite):
    def __init__(self, y=-1):
        pygame.sprite.Sprite.__init__(self)
        if y == -1:
            self.coor = (self.x, self.y) = (randint(0, 490), randint(0, 500))
        else:
            self.coor = (self.x, self.y) = (randint(0, 490), y)
        self.height = 3

    for koor in platf_koords:
        pass
        #if koor[1] <= self.height:
         #   koor[1] = a
        #else:
         #   koor[1] = -30

    def below_wind(self):
        if self.y > 600:
            self.coor = (self.x, self.y) = (randint(0, 1800), 0)

    def get_pos(self):
        return self.coor

    def get_widt(self):
        return 90

    def get_heigh(self):
        return 60


class Land(Platforms):
    def __init__(self):
        super().__init__()
        self.coor = self.x, self.y = 0, 550

    def down(self):
        if self.y >= 0:
            self.y += self.height
        self.coor = (self.x, self.y)

    def get_widt(self):
        return 500

    def get_heigh(self):
        return 50
