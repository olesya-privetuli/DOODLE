from random import randint
from constans import numb_of_plate, width, platf_width, platf_heights, height, new_h


class Plate_koor:
    def __init__(self):
        self.sh = 5
        self.dow = False
        self.platf_koords = [(0, 550)]
        self.platf_jump = [True]
        for i in range(numb_of_plate):
            self.platf_koords.append((randint(0, width - platf_width), platf_heights[i]))
            self.platf_jump.append(False)

    def update(self):
        self.platf_koords = [(0, 550)]
        self.platf_jump = [True]
        for i in range(numb_of_plate):
            self.platf_koords.append((randint(0, width - platf_width), platf_heights[i]))
            self.platf_jump.append(False)

    def down(self, shift):
        for koor in range(len(self.platf_koords)):
            if self.platf_koords[koor][1] <= height or koor == 0 and \
                    self.platf_koords[0][1] < height * 3:
                self.platf_koords[koor] = self.platf_koords[koor][0], self.platf_koords[koor][1] + shift
            elif koor != 0:
                self.platf_koords[koor] = randint(0, width - platf_width), new_h
                self.platf_jump[koor] = False

    def get_pos(self, ind):
        return self.platf_koords[ind]

    def pl_koor(self):
        return self.platf_koords

    def pl_jump(self):
        return self.platf_jump

    def change_h(self):
        if self.dow:
            self.down(self.sh)

    def alow(self, log):
        self.dow = log
