from Board import Board

def clr(size):
    for i in range(size):
        print("\033[1F", end="")
    print("\r", end = "")

def print_board(board: Board):
    for i in range(board.size ** 2):
        if i and not i % board.size:
            print()

        alive = board.fields[i].alive
        print("#", end = ' ') if alive else print(".", end = ' ')

def print_neighbour_indexes(board: Board, idx_to_print):
    print(board.fields[idx_to_print].neighbours)