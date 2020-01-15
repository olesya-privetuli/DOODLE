class Board:
    def __init__(self):
        self.width = 2
        self.height = 2
        self.widt_size = 250
        self.heigh_size = 300
        self.board = []
        self.place = []
        self.lst()
        self.col = [0 for _ in range(self.width * self.height)]

    def lst(self):
        self.board = []
        c = 0
        for i in range(self.height):
            r = 0
            for j in range(self.width):
                self.board.append((r, c, self.widt_size, self.heigh_size))
                self.place.append((i, j))
                r += self.widt_size
            c += self.heigh_size

    def render(self):
        return self.board

    def get_posit(self, cell_coords):
        lis = []
        for i in range(len(self.board)):
            if self.board[i][0] < cell_coords[0] < self.board[i][0] + self.widt_size and \
                    self.board[i][1] < cell_coords[1] < self.board[i][1] + self.heigh_size:
                lis.append(self.place[i])
        return lis

    def on_click(self, cell_coords):
        for i in self.get_posit(cell_coords):
            if self.col[self.place.index(i)] == 0:
                self.col[self.place.index(i)] = 1
            elif self.col[self.place.index(i)] == 1:
                self.col[self.place.index(i)] = 2
            else:
                self.col[self.place.index(i)] = 0

    def picture(self, pos):
        if self.get_posit(pos) == [(0, 0)]:
            return 0
        elif self.get_posit(pos) == [(0, 1)]:
            return 1
        elif self.get_posit(pos) == [(1, 0)]:
            return 2
        elif self.get_posit(pos) == [(1, 1)]:
            return 3
