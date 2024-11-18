from Field import Field


class INeighbouring:
    def __init__(self, size):
        self.size = size

    def set_neighbours(self, field: Field):
        raise Exception("not implemented")