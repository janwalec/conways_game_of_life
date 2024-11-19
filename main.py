import cProfile
import pstats
import random

from ConsoleDisplayer import print_board
from GameManager.IGameManager import IGameManager
from GameManager.MultiProcessingGameManager import MultiProcessingGameManager
from GameManager.ProceduralGameManager import ProceduralGameManager
from Neighbouring.Neighbouring2D import Neighbouring2D
from Neighbouring.NeighbouringCylinder import NeighbouringCylinder
from PygameDisplay import PygameDisplay
import time

def init_gm(s, chance):
        #random.seed(42)

        n = Neighbouring2D(s)
        #n = NeighbouringCylinder(s)

        gm = MultiProcessingGameManager(s, n, chance)

        return gm


def test_time(gm: IGameManager, num_of_iter):
    time_start = time.time()

    for i in range(num_of_iter):
        gm.do_moves()
        print(i)

    print(round(time.time() - time_start, 3))

if __name__ == "__main__":
    s = 500
    ch = 0.2
    gm = init_gm(s, ch)
    gm.set_life()
    #gm.board.set_field_alive(s ** 2 // 2 + s//2, 1)

    #test_time(gm, 20)
    #cProfile.run("test_time(gm, 30)", "my_func_stats")
    #p = pstats.Stats("my_func_stats")
    #p.sort_stats("cumulative").print_stats()
    pd = PygameDisplay(1000, gm)
    pd.run()



#6.295 - 50 iters, no multiprocessing, every neighbour - 8 fields