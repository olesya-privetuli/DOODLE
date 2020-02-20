from random import randint
from constans import numb_of_plate, width, platf_width, platf_heights, height, new_h, pl_heigh
from constans import land_w, land_h


class Plate_coor:
    def __init__(self):
        self.sh = 5
        self.dow = False
        self.platf_coords = [(0, 550)]
        self.platf_jump = [True]
        for i in range(numb_of_plate):
            self.platf_coords.append((randint(0, width - platf_width), platf_heights[i]))
            self.platf_jump.append(False)

    def update(self):
        self.platf_coords = [(0, 550)]
        self.platf_jump = [True]
        for i in range(numb_of_plate):
            self.platf_coords.append((randint(0, width - platf_width), platf_heights[i]))
            self.platf_jump.append(False)

    def down(self, shift):
        for koor in range(len(self.platf_coords)):
            if self.platf_coords[koor][1] <= height or koor == 0 and \
                    self.platf_coords[0][1] < height * 3:
                self.platf_coords[koor] = self.platf_coords[koor][0], self.platf_coords[koor][1] + shift
            elif koor != 0:
                self.platf_coords[koor] = randint(0, width - platf_width), new_h
                self.platf_jump[koor] = False

    def get_pos(self, ind):
        return self.platf_coords[ind]

    def pl_coor(self):
        return self.platf_coords

    def pl_jump(self):
        return self.platf_jump

    def change_h(self):
        if self.dow:
            self.down(self.sh)

    def alow(self, log):
        self.dow = log


class Platforms:
    def __init__(self):
        self.coor = self.x, self.y = 0, 0

    def get_width(self):
        return platf_width

    def get_height(self):
        return pl_heigh


class Land(Platforms):
    def __init__(self):
        super().__init__()
        self.y = 0, 550

    def get_width(self):
        return land_w

    def get_height(self):
        return land_h
