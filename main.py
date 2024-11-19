import cProfile
import pstats

from ConsoleDisplayer import print_board
from GameManager.IGameManager import IGameManager
from GameManager.MultiProcessingGameManager import MultiProcessingGameManager
from GameManager.ProceduralGameManager import ProceduralGameManager
from Neighbouring.Neighbouring2D import Neighbouring2D
from Neighbouring.NeighbouringCylinder import NeighbouringCylinder
from PygameDisplay import PygameDisplay
import time

def init_gm():
        s = 200
        chance = 0.2
        n = Neighbouring2D(s)
        # n = NeighbouringCylinder(s)

        gm = ProceduralGameManager(s, n, chance)

        # cProfile.run("test_time(gm, 3)", "my_func_stats")
        # p = pstats.Stats("my_func_stats")
        # p.sort_stats("cumulative").print_stats()
        return gm


def test_time(gm: IGameManager, num_of_iter):
    time_start = time.time()

    for i in range(num_of_iter):
        gm.do_moves()
        print(i)

    print(round(time.time() - time_start, 3))

if __name__ == "__main__":
    gm = init_gm()
    gm.set_life()
    #test_time(gm, 50)
    pd = PygameDisplay(1000, gm)
    pd.run()



#6.295 - 50 iters, no multiprocessing, every neighbour - 8 fields