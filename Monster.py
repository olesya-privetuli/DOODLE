from random import randint
from constans import monsters_coords

height = 600
monster_height = 60
plate_height = 200


class Monster:
    def __init__(self):
        self.x, self.y = -1 * monster_height, randint(0, height - monster_height)
        self.step = 2

    def fly(self):
        self.x += self.step

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def update(self):
        self.x, self.y = -1 * monster_height, randint(0, height - monster_height)