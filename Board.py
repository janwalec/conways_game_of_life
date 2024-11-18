from random import randint
from Field import Field
from Neighbouring.INeighbouring import INeighbouring


class Board:
    def __init__(self, size, neighbouring: INeighbouring):
        self.neighbouring = neighbouring
        self.fields = self.init_fields(size)
        self.size = size

    def init_fields(self, size):
        if size <= 1:
            raise Exception("size must be greater than 1")

        b = []
        for i in range(size ** 2):
            f = Field(i)
            f.set_neighbours(self.neighbouring.set_neighbours(f))
            b.append(f)
        return b


    def randomize_life(self, perc: float):
        upper_bound = int(perc * 100)
        for i in range(self.size ** 2):
            r = randint(0, 100)
            if r < upper_bound:
                self.fields[i].set_alive(1)
            else:
                self.fields[i].set_alive(0)
