import os
import time
from ConsoleDisplayer import *
from GameManager import GameManager
from Neighbouring.Neighbouring2D import Neighbouring2D
from PygameDisplay import PygameDisplay

s = 100
chance = 0.0
n = Neighbouring2D(s)
gm = GameManager(s, n, chance)
gm.set_life()


pd = PygameDisplay(1000, gm)
pd.run()


