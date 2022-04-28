"""

В этом модуле созданы матрица и массив,
используемые в других заданиях

"""

from random import randint


SIZE = 20
SIZE_M = 5
SIZE_N = 5
MIN_ITEM = 0
MIN_N_ITEM = - 100
MAX_ITEM = 100
matrix = [[randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)] for _ in range(SIZE_N)]
array = [randint(MIN_N_ITEM, MAX_ITEM) for _ in range(SIZE)]


if __name__ == '__main__':

    print(*matrix, sep='\n')
    print(array)


