from constans import platf_width, pl_heigh, land_w, land_h


class Platforms:
    def __init__(self):
        self.coor = self.x, self.y = (0, 0)

    def get_width(self):
        return platf_width

    def get_height(self):
        return pl_heigh


class Land(Platforms):
    def __init__(self):
        super().__init__()
        self.coor = self.x, self.y = 0, 550

    def get_width(self):
        return land_w

    def get_height(self):
        return land_h
