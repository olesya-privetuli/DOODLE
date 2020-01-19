from random import randint
from constans import monster_start

height = 600
monster_height = 60
plate_height = 200


class Monster:
    def __init__(self):
        self.x, self.y = -1 * monster_height, randint(0, monster_start)
        self.shift = 5
        self.step = 2
        self.dow = False

    def allow(self, log):
        self.dow = log

    def down(self):
        if self.dow:
            self.y += self.shift

    def fly(self):
        self.x += self.step

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def update(self):
        self.x, self.y = -1 * monster_height, randint(0, monster_start)
