'''import multiprocessing

from Board import Board
from Field import Field
from Neighbouring.INeighbouring import INeighbouring


class xGameManager:
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

    @staticmethod
    def process_field(args):
        i, alive, alive_neighbours_num, die, spawn = args
        kill_this = []
        spawn_this = []

        match alive:
            case 0:  # dead cell
                for condition in spawn:
                    if alive_neighbours_num - condition == 0:
                        spawn_this.append(i)
                        break

            case 1:  # live cell
                for condition in die:
                    if alive_neighbours_num - condition == 0:
                        kill_this.append(i)
                        break

        return kill_this, spawn_this

    def do_moves(self):
        to_kill = [] # cells that would be killed
        to_spawn = [] # cells that would be spawned


        for i in range(self.size ** 2):
            field = self.board.fields[i]
            alive = field.alive
            cells_around = self.count_neighbours(field)

            kill_this, spawn_this = self.process_field((i, alive, cells_around))

            to_kill.extend(kill_this)
            to_spawn.extend(spawn_this)

        for k in to_kill:
            self.board.fields[k].set_alive(0)
        for s in to_spawn:
            self.board.fields[s].set_alive(1)


    def do_moves_multiprocessing(self):
        tasks = [
            (i, field.alive, self.count_neighbours(field), self.die, self.spawn)
            for i, field in enumerate(self.board.fields)
        ]

        with multiprocessing.Pool() as pool:
            results = pool.map(self.process_field, tasks)

        # Collect results
        to_kill = []
        to_spawn = []

        for kill_this, spawn_this in results:
            to_kill.extend(kill_this)
            to_spawn.extend(spawn_this)

        for k in to_kill:
            self.board.fields[k].set_alive(0)
        for s in to_spawn:
            self.board.fields[s].set_alive(1)

'''