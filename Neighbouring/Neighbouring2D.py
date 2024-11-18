from Field import Field
from Neighbouring.INeighbouring import INeighbouring


class Neighbouring2D(INeighbouring):
    def __init__(self, size):
        super().__init__(size)

    def set_neighbours(self, field: Field):
        neighbours = []
        idx = field.index
        s = self.size
        row, col = divmod(idx, s)
        d = [-1, 0, 1]

        for d_y in d:
            for d_x in d:
                nr, nc = row + d_x, col + d_y
                if 0 <= nr < s and 0 <= nc < s and nr * s + nc != idx:
                    neighbours.append((nr * s + nc))

        return neighbours
