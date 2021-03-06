from constans import dood_w, width, jump_h, dood_shift, height, dood_h


class Doodle:
    def __init__(self):
        self.coor = (self.x, self.y) = (210, 500)
        self.height = jump_h
        self.flying = True

    def jump(self):
        if self.flying:
            self.y += 0.9 * self.height
        else:
            self.y -= 1.4 * self.height
        self.coor = (self.x, self.y)

    def right(self):
        self.x += 5
        if self.x + 0.5 * dood_w > width:
            self.x = - 0.5 * dood_w
        self.coor = (self.x, self.y)

    def left(self):
        self.x -= 5
        if self.x + 0.5 * dood_w < 0:
            self.x = width - 0.5 * dood_w
        self.coor = (self.x, self.y)

    def get_posit(self):
        return self.coor

    def check_end(self, log=False):
        if self.y > height - dood_h:
            return True
        elif log:
            self.coor = (self.x, self.y) = (210, 500)

    def fly(self):
        if self.flying:
            self.flying = False
        else:
            self.flying = True

    def get_fly(self):
        return self.flying

    def down(self):
        self.y += dood_shift
        self.coor = self.x, self.y
