from multiprocessing import Pool
from random import randint


def in_array():
    arr = []
    for i in range(10000):
        arr.append(randint(0, 6))

    return arr


def some_expression(i):
    return i ** 2 ** 2


if __name__ == '__main__':
    pool = Pool(8)
    arr = in_array()
    print(arr)
    res = pool.map(some_expression, arr)
    print(res)