import sys
# Add new folders
sys.path.insert(1, './algorithms')
sys.path.insert(2, './tests')
# Max recursion limit (default: 1000)
sys.setrecursionlimit(100000)

from quick_sort import quick_sort
from tower_of_hanoi import hanoi_tower
from list_gen import random_generator, descending_generator, ascending_generator, equal_generator
from quick_sort_med3 import quick_sort_m3

import random
import timeit

MAX = 5000
COUNTER = 0

RANDOM_LIST = random_generator(10000)
GROWING_LIST = ascending_generator(10000)
DECREASING_LIST = descending_generator(10000)
EQUAL_LIST = equal_generator(10000)

RANDOM_LIST2 = random_generator(10000)
GROWING_LIST2 = ascending_generator(10000)
DECREASING_LIST2 = descending_generator(10000)
EQUAL_LIST2 = equal_generator(10000)

def test ():
    """Test function"""
    if COUNTER == 1:
        quick_sort(RANDOM_LIST, 0, MAX)
        print("LISTA ALEATORIA: ", end = '')
    if COUNTER == 2:
        quick_sort(GROWING_LIST, 0, MAX)
        print("LISTA CRESCENTE: ", end = '')
    if COUNTER == 3:
        quick_sort(DECREASING_LIST, 0, MAX)
        print("LISTA DECRESCENTE: ", end = '')
    if COUNTER == 4:
        print("LISTA IDENTICA: ", end = '')
        quick_sort(EQUAL_LIST, 0, MAX)

    if COUNTER == 5:
        quick_sort_m3(RANDOM_LIST2, 0, MAX)
        print("LISTA ALEATORIA: ", end = '')
    if COUNTER == 6:
        quick_sort_m3(GROWING_LIST2, 0, MAX)
        print("LISTA CRESCENTE: ", end = '')
    if COUNTER == 7:
        quick_sort_m3(DECREASING_LIST2, 0, MAX)
        print("LISTA DECRESCENTE: ", end = '')
    if COUNTER == 8:
        print("LISTA IDENTICA: ", end = '')
        quick_sort_m3(EQUAL_LIST2, 0, MAX)

    if COUNTER == 9:
        print("Torre com 20 discos: ", end = '')
        hanoi_tower(20, 1, 2, 3)
    if COUNTER == 10:
        print("Torre com 25 discos: ", end = '')
        hanoi_tower(25, 1, 2, 3)
    if COUNTER == 11:
        print("Torre com 26 discos: ", end = '')
        hanoi_tower(26, 1, 2, 3)
    if COUNTER == 12:
        print("Torre com 27 discos: ", end = '')
        hanoi_tower(27, 1, 2, 3)
        

if __name__ == "__main__":

    print("Quick Sort:")
    for i in range(4):
        COUNTER = COUNTER + 1
        print(timeit.timeit("test()", setup="from __main__ import test",number = 1))

    print("")
    print("Quick Sort com medianas de 3:")
    for i in range(4):
        COUNTER = COUNTER + 1
        print(timeit.timeit("test()", setup="from __main__ import test",number = 1))

    print("")
    print("Torre de Hanoi: ")
    for i in range(4):
        COUNTER = COUNTER + 1
        print(timeit.timeit("test()", setup="from __main__ import test",number = 1))
