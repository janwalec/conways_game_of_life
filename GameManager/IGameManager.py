from Board import Board
from Field import Field
from Neighbouring.INeighbouring import INeighbouring


class IGameManager:
    def __init__(self, size, neighbouring: INeighbouring, chance):
        self.size = size
        self.board = Board(size, neighbouring)
        self.die, self.spawn = self.set_rules()
        self.chance = chance

    def set_life(self, ran=None):
        if ran is None:
            self.board.randomize_life(self.chance)
        else:
            print("AAA")

    @staticmethod
    def set_rules():
        # die if less than 2 neighbours alive
        # die if more than 3 neighbours alive
        die = [0, 1, 4, 5, 6, 7, 8]
        # spawn if exactly 3 live neighbours around
        spawn = [3]
        return die, spawn

    def count_neighbours(self, field: Field):
        cntr = 0
        for idx in field.neighbours:
            if self.board.fields[idx].alive:
                cntr += 1
        return cntr

    def do_moves(self):
        raise Exception("Not implemented")

    def process_field(self, args):
        raise Exception("Not implemented")