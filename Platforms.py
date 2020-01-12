from random import randint
import pygame
from constans import platf_koords, height, numb_of_clouds, max_h, jump_h, platf_width, pl_heigh
from constans import land_w, land_h


class Platforms(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def down(self, koor_ind):
        for koor in platf_koords:
            for i in range(1, numb_of_clouds + 1):
                if platf_koords[i][1] <= height:
                   platf_koords[i] = platf_koords[i][0], platf_koords[i][1] + max_h * jump_h
                else:
                    platf_koords[i] = platf_koords[i][0], -30

    def below_wind(self, ind):
        if platf_koords[ind][1] > 600:
            self.coor = (self.x, self.y) = (randint(0, 1800), 0)

    def get_pos(self, ind):
        return platf_koords[ind]

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
