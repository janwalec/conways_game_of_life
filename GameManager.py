from Board import Board
from Field import Field
from Neighbouring.INeighbouring import INeighbouring


class GameManager:
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

    def do_move(self):
        to_kill = [] # cells that would be killed
        to_spawn = [] # cells that would be spawned
        for i in range(self.size ** 2):
            field = self.board.fields[i]
            alive = field.alive
            cells_around = self.count_neighbours(field)

            match alive:
                case 0: # dead cell
                    for condition in self.spawn:
                        if cells_around - condition == 0:
                            to_spawn.append(i)
                            break

                case 1: # live cell
                    for condition in self.die:
                        if cells_around - condition == 0:
                            to_kill.append(i)

        for k in to_kill:
            self.board.fields[k].set_alive(0)
        for s in to_spawn:
            self.board.fields[s].set_alive(1)



    def count_neighbours(self, field: Field):
        cntr = 0
        for idx in field.neighbours:
            if self.board.fields[idx].alive:
                cntr += 1
        return cntr