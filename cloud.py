import random
from constans import numb_of_clouds, all_speeds, cloud_koords


class Cloud:
    def __init__(self):
        self.width, self.height = 500, 600

    def change_h(self):
        for koor in cloud_koords:
            if koor[1] <= self.height:
                a = koor[1] + all_speeds[cloud_koords.index(koor)]
                koor[1] = a
            else:
                koor[1] = -30
