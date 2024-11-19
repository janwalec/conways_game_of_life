
from multiprocessing import Pool
import os
from copy import deepcopy

from GameManager.IGameManager import IGameManager
from Neighbouring.INeighbouring import INeighbouring


class MultiProcessingGameManager(IGameManager):
    def __init__(self, size, neighbouring: INeighbouring, chance):
        super().__init__(size, neighbouring, chance)
        self.chunk_size = 100
        self.chunks = self.split_into_chunks()
        self.pool = Pool(8)


    def split_into_chunks(self):
        return [self.board.fields[i:i + self.chunk_size] for i in range(0, len(self.board.fields), self.chunk_size)]

    def process_chunk(self, chunk):
        to_kill = []
        to_spawn = []
        for field in chunk:
            k, s = self.process_field(field)
            to_kill.extend(k)
            to_spawn.extend(s)

        return to_kill#, to_spawn


    def process_field(self, field):

        i = field.index
        alive = field.alive
        alive_neighbours_num = self.count_neighbours(field)

        kill_this = []
        spawn_this = []

        match alive:
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


    def do_moves(self):
        to_kill = []
        to_spawn = []

        res = self.pool.map(self.process_chunk, self.chunks)

        # Teraz results jest listą krotek (to_kill, to_spawn)
        for result in res:
            k, s = result.get()
            to_kill.extend(k)
            to_spawn.extend(s)

        for k in to_kill:
            self.board.fields[k].set_alive(0)
        for s in to_spawn:
            self.board.fields[s].set_alive(1)

    def close_pool(self):
        # Zamykanie puli, kiedy już nie jest potrzebna
        self.pool.close()
        self.pool.join()
