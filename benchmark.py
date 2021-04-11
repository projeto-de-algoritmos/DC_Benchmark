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
COUNTER = -1

RANDOM_LIST = random_generator(10000)
GROWING_LIST = ascending_generator(10000)
DECREASING_LIST = descending_generator(10000)
EQUAL_LIST = equal_generator(10000)

RANDOM_LIST2 = random_generator(10000)
GROWING_LIST2 = ascending_generator(10000)
DECREASING_LIST2 = descending_generator(10000)
EQUAL_LIST2 = equal_generator(10000)

COMMAND_LIST = []
PRINT_LIST = []

def timer_test():
    print(timeit.timeit("test()", setup="from __main__ import test",number = 1))

def test ():
    """Test function"""
    print(PRINT_LIST[COUNTER], end = '')
    eval(COMMAND_LIST[COUNTER])

if __name__ == "__main__":

    COMMAND_LIST.append('quick_sort(RANDOM_LIST, 0, MAX)')
    PRINT_LIST.append("LISTA ALEATORIA: ")

    COMMAND_LIST.append('quick_sort(GROWING_LIST, 0, MAX)')
    PRINT_LIST.append("LISTA CRESCENTE: ")

    COMMAND_LIST.append('quick_sort(DECREASING_LIST, 0, MAX)')
    PRINT_LIST.append("LISTA DECRESCENTE: ")

    COMMAND_LIST.append('quick_sort(EQUAL_LIST, 0, MAX)')
    PRINT_LIST.append("LISTA IDENTICA: ")

    COMMAND_LIST.append('quick_sort_m3(RANDOM_LIST2, 0, MAX)')
    PRINT_LIST.append("LISTA ALEATORIA: ")

    COMMAND_LIST.append('quick_sort_m3(GROWING_LIST2, 0, MAX)')
    PRINT_LIST.append("LISTA CRESCENTE: ")

    COMMAND_LIST.append('quick_sort_m3(DECREASING_LIST2, 0, MAX)')
    PRINT_LIST.append("LISTA DECRESCENTE: ")

    COMMAND_LIST.append('quick_sort_m3(EQUAL_LIST2, 0, MAX)')
    PRINT_LIST.append("LISTA IDENTICA: ")

    COMMAND_LIST.append('hanoi_tower(20, 1, 2, 3)')
    PRINT_LIST.append("Torre com 20 discos: ")

    COMMAND_LIST.append('hanoi_tower(25, 1, 2, 3)')
    PRINT_LIST.append("Torre com 25 discos: ")

    COMMAND_LIST.append('hanoi_tower(26, 1, 2, 3)')
    PRINT_LIST.append("Torre com 26 discos: ")

    COMMAND_LIST.append('hanoi_tower(27, 1, 2, 3)')
    PRINT_LIST.append("Torre com 27 discos: ")

    for i in range(len(COMMAND_LIST)):
        if COUNTER == -1:
            print("Quick Sort:")
        if COUNTER == 3:
            print("")
            print("Quick Sort Mediana de 3:")
        if COUNTER == 7:
            print("")
            print("Torre de Hanoi:")

        COUNTER = COUNTER + 1
        timer_test()