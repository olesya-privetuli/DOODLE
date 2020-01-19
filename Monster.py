from random import randint
from constans import monster_start

height = 600
monster_height = 60
plate_height = 200


class Monster:
    def __init__(self):
        self.x, self.y = -1 * monster_height - 20, randint(0, monster_start)
        self.shift = 5
        self.step = 2
        self.dow = False
        self.coords = (self.x, self.y)

    def allow(self, log):
        self.dow = log

    def down(self):
        if self.dow:
            self.y += self.shift
            self.coords = (self.x, self.y)

    def fly(self):
        self.x += self.step
        self.coords = (self.x, self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def update(self):
        self.x, self.y = -1 * monster_height - 20, randint(0, monster_start)
        self.coords = (self.x, self.y)

    def get_all_coords(self):
        return self.x, self.y
