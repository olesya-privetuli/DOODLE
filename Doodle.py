from Background import Background


class Doodle:
    def __init__(self):
        self.coor = (self.x, self.y) = (210, 500)
        self.height = -6
        self.flying = True

    def jump(self):
        if self.flying:
            self.y += self.height
        else:
            self.y -= self.height
        self.coor = (self.x, self.y)

    def right(self):
        self.x += 5
        if self.x + 45 > 500:
            self.x = -45
        elif self.x + 45 < 0:
            self.x = 500
        self.coor = (self.x, self.y)

    def left(self):
        self.x -= 5
        self.coor = (self.x, self.y)

    def get_posit(self):
        return self.coor

    def check_end(self):
        if self.y > 540 or self.collision():
            Background.get_result()

    def collision(self):
        pass

    def fly(self):
        if self.flying:
            self.flying = False
        else:
            self.flying = True