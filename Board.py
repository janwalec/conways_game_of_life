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
                self.set_field_alive(i, 1)
            else:
                self.set_field_alive(i, 0)

    def set_field_alive(self, index, alive):
        field = self.fields[index]

        was_alive = field.alive
        field.set_alive(alive)

        if not was_alive and alive:
            for neighbour_index in field.neighbours:
                self.fields[neighbour_index].number_of_alive_neighbours += 1
        elif was_alive and not alive:
            for neighbour_index in field.neighbours:
                self.fields[neighbour_index].number_of_alive_neighbours -= 1



