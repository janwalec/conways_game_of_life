
class Field:
    def __init__(self, index: int):
        self.index = index
        self.neighbours = []
        self.alive = 0

    def set_alive(self, alive):
        self.alive = alive

    def set_neighbours(self, neighbours):
        self.neighbours = neighbours
