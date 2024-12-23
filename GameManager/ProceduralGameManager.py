from GameManager.IGameManager import IGameManager
from Neighbouring.INeighbouring import INeighbouring


class ProceduralGameManager(IGameManager):
    def __init__(self, size, neighbouring: INeighbouring, chance):
        super().__init__(size, neighbouring, chance)



    def process_field(self, args):
        field = args
        i = field.index
        alive = field.alive
        alive_neighbours_num = field.number_of_alive_neighbours

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
        to_kill = [] # cells that would be killed
        to_spawn = [] # cells that would be spawned


        for i in range(self.size ** 2):
            field = self.board.fields[i]

            kill_this, spawn_this = self.process_field(field)

            to_kill.extend(kill_this)
            to_spawn.extend(spawn_this)

        for k in to_kill:
            self.board.set_field_alive(k, 0)
        for s in to_spawn:
            self.board.set_field_alive(s, 1)

