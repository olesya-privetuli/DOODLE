from random import randint

height = 600
monster_height = 60
plate_height = 200


class Monster:
    def __init__(self):
        self.coor = self.x, self.y = (0, randint(0, height - monster_height))
        self.step = 5

    def fly(self):
        self.x += self.step
        self.coor = self.x, self.y

    def down(self):
        self.y += plate_height
        self.coor = self.x, self.y