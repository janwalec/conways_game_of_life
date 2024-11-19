from concurrent.futures import ThreadPoolExecutor
from itertools import islice
from multiprocessing import Pool
import os
from copy import deepcopy

from GameManager.IGameManager import IGameManager
from Neighbouring.INeighbouring import INeighbouring


class MultiProcessingGameManager(IGameManager):
    def __init__(self, size, neighbouring: INeighbouring, chance):
        super().__init__(size, neighbouring, chance)
        num_of_workers = max_workers=os.cpu_count()
        self.chunk_size = size ** 2 // num_of_workers

        self.chunks = self.split_into_chunks(self.chunk_size)
        self.executor = ThreadPoolExecutor(max_workers=num_of_workers)


    def process_chunk(self, chunk):
        to_kill = []
        to_spawn = []
        for f in chunk:
            k, s = self.process_field(f)
            if k:
                to_kill.append(f.index)
            elif s:
                to_spawn.append(f.index)
        return to_kill, to_spawn



    def process_field(self, args):
        field = args
        alive_neighbours_num = self.count_neighbours(field)
        i = field.index

        kill_this = []
        spawn_this = []

        match field.alive:
            case 0:  # dead cell
                for condition in self.spawn:
                    if alive_neighbours_num - condition == 0:
                        spawn_this.append(i)
                        break

            case 1:  # live cell
                for condition in self.die:
                    if alive_neighbours_num - condition == 0:
                        kill_this.append(i)
                        break
        return kill_this, spawn_this

    def split_into_chunks(self, chunk_size):
        return [self.board.fields[i:i + chunk_size] for i in range(0, len(self.board.fields), chunk_size)]

    def do_moves(self):

        res = self.executor.map(self.process_chunk, self.chunks)

        for k, s in res:
            for kill_pos in k:
                self.board.fields[kill_pos].set_alive(0)
            for spawn_pos in s:
                self.board.fields[spawn_pos].set_alive(1)

    def __getstate__(self):
        self_dict = self.__dict__.copy()
        del self_dict['pool']
        return self_dict

    def __setstate__(self, state):
        self.__dict__.update(state)


