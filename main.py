from GameManager import GameManager
from Neighbouring.Neighbouring2D import Neighbouring2D
from Neighbouring.NeighbouringCylinder import NeighbouringCylinder
from PygameDisplay import PygameDisplay

s = 100
chance = 0.2
n = Neighbouring2D(s)
# n = NeighbouringCylinder(s)

gm = GameManager(s, n, chance)
gm.set_life()


pd = PygameDisplay(1000, gm)
pd.run()


