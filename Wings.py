from random import randint
from Background import Background


class Wings:
    def __init__(self):
        self.height = Background.get_result
        self.coor = (self.x, self.y) = (randint(0, 500), randint(0, 600))

    def get_coor(self):
        return self.coor