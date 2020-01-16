from random import randint
import pygame
from constans import platf_koords, height, width, max_h, jump_h, platf_width, pl_heigh, platf_jump
from constans import new_h
from constans import land_w, land_h


class Platforms(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.coor = self.x, self.y = (0, 0)

    def down(self):
        for koor in range(len(platf_koords)):
            if platf_koords[koor][1] <= height:
                platf_koords[koor] = platf_koords[koor][0], platf_koords[koor][1] + max_h * jump_h
            elif koor != 0 and platf_koords[0] <= width + Land().get_heigh():
                platf_koords[koor] = randint(0, width), new_h
                platf_jump[koor] = False

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
