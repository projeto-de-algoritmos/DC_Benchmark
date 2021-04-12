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
from binary_search import binary_search
from merge_sort import merge_sort

import random
import timeit

MAX = 5000
MAX2 = 10000
COUNTER = -1

RANDOM_LIST = random_generator(MAX + 1)
GROWING_LIST = ascending_generator(MAX + 1)
DECREASING_LIST = descending_generator(MAX + 1)
EQUAL_LIST = equal_generator(MAX + 1)

RANDOM_LIST2 = random_generator(MAX + 1)
GROWING_LIST2 = ascending_generator(MAX + 1)
DECREASING_LIST2 = descending_generator(MAX + 1)
EQUAL_LIST2 = equal_generator(MAX + 1)

RANDOM_LIST3 = random_generator(MAX2 + 1)
GROWING_LIST3 = ascending_generator(MAX2 + 1)
DECREASING_LIST3 = descending_generator(MAX2 + 1)
EQUAL_LIST3 = equal_generator(MAX2 + 1)

RANDOM_LIST4 = random_generator(MAX2 + 1)
GROWING_LIST4 = ascending_generator(MAX2 + 1)
DECREASING_LIST4 = descending_generator(MAX2 + 1)
EQUAL_LIST4 = equal_generator(MAX2 + 1)

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

    COMMAND_LIST.append('merge_sort(RANDOM_LIST, 0, MAX)')
    PRINT_LIST.append("LISTA ALEATORIA: ")

    COMMAND_LIST.append('merge_sort(GROWING_LIST, 0, MAX)')
    PRINT_LIST.append("LISTA CRESCENTE: ")

    COMMAND_LIST.append('merge_sort(DECREASING_LIST, 0, MAX)')
    PRINT_LIST.append("LISTA DECRESCENTE: ")

    COMMAND_LIST.append('merge_sort(EQUAL_LIST, 0, MAX)')
    PRINT_LIST.append("LISTA IDENTICA: ")

    COMMAND_LIST.append('quick_sort_m3(RANDOM_LIST2, 0, MAX)')
    PRINT_LIST.append("LISTA ALEATORIA: ")

    COMMAND_LIST.append('quick_sort_m3(GROWING_LIST2, 0, MAX)')
    PRINT_LIST.append("LISTA CRESCENTE: ")

    COMMAND_LIST.append('quick_sort_m3(DECREASING_LIST2, 0, MAX)')
    PRINT_LIST.append("LISTA DECRESCENTE: ")

    COMMAND_LIST.append('quick_sort_m3(EQUAL_LIST2, 0, MAX)')
    PRINT_LIST.append("LISTA IDENTICA: ")

    COMMAND_LIST.append('quick_sort(RANDOM_LIST3, 0, MAX2)')
    PRINT_LIST.append("LISTA ALEATORIA: ")

    COMMAND_LIST.append('quick_sort(GROWING_LIST3, 0, MAX2)')
    PRINT_LIST.append("LISTA CRESCENTE: ")

    COMMAND_LIST.append('quick_sort(DECREASING_LIST3, 0, MAX2)')
    PRINT_LIST.append("LISTA DECRESCENTE: ")

    COMMAND_LIST.append('quick_sort(EQUAL_LIST3, 0, MAX2)')
    PRINT_LIST.append("LISTA IDENTICA: ")

    COMMAND_LIST.append('merge_sort(RANDOM_LIST3, 0, MAX2)')
    PRINT_LIST.append("LISTA ALEATORIA: ")

    COMMAND_LIST.append('merge_sort(GROWING_LIST3, 0, MAX2)')
    PRINT_LIST.append("LISTA CRESCENTE: ")

    COMMAND_LIST.append('merge_sort(DECREASING_LIST3, 0, MAX2)')
    PRINT_LIST.append("LISTA DECRESCENTE: ")

    COMMAND_LIST.append('merge_sort(EQUAL_LIST3, 0, MAX2)')
    PRINT_LIST.append("LISTA IDENTICA: ")

    COMMAND_LIST.append('quick_sort_m3(RANDOM_LIST4, 0, MAX2)')
    PRINT_LIST.append("LISTA ALEATORIA: ")

    COMMAND_LIST.append('quick_sort_m3(GROWING_LIST4, 0, MAX2)')
    PRINT_LIST.append("LISTA CRESCENTE: ")

    COMMAND_LIST.append('quick_sort_m3(DECREASING_LIST4, 0, MAX2)')
    PRINT_LIST.append("LISTA DECRESCENTE: ")

    COMMAND_LIST.append('quick_sort_m3(EQUAL_LIST4, 0, MAX2)')
    PRINT_LIST.append("LISTA IDENTICA: ")

    COMMAND_LIST.append('hanoi_tower(20, 1, 2, 3)')
    PRINT_LIST.append("Torre com 20 discos: ")

    COMMAND_LIST.append('hanoi_tower(25, 1, 2, 3)')
    PRINT_LIST.append("Torre com 25 discos: ")

    COMMAND_LIST.append('hanoi_tower(26, 1, 2, 3)')
    PRINT_LIST.append("Torre com 26 discos: ")

    COMMAND_LIST.append('hanoi_tower(27, 1, 2, 3)')
    PRINT_LIST.append("Torre com 27 discos: ")

    COMMAND_LIST.append('binary_search(RANDOM_LIST, 0, MAX, 5)')
    PRINT_LIST.append("(5000 elementos - valor existente): ")

    COMMAND_LIST.append('binary_search(RANDOM_LIST4, 0, MAX2, 5)')
    PRINT_LIST.append("(10000 elementos - valor existente): ")

    COMMAND_LIST.append('binary_search(GROWING_LIST, 0, MAX, MAX+2)')
    PRINT_LIST.append("(5000 elementos - valor inexistente): ")

    COMMAND_LIST.append('binary_search(GROWING_LIST, 0, MAX2, -1)')
    PRINT_LIST.append("(10000 elementos - valor inexistente): ")

    for i in range(len(COMMAND_LIST)):
        if COUNTER == -1:
            print("Quick Sort: (5000 elementos)")
        if COUNTER == 3:
            print("")
            print("Merge Sort: (5000 elementos)")
        if COUNTER == 7:
            print("")
            print("Quick Sort Mediana de 3: (5000 elementos)")
        if COUNTER == 11:
            print("")
            print("Quick Sort: (10000 elementos)")
        if COUNTER == 15:
            print("")
            print("Merge Sort: (10000 elementos)")
        if COUNTER == 19:
            print("")
            print("Quick Sort Mediana de 3: (10000 elementos)")
        if COUNTER == 23:
            print("")
            print("Torre de Hanoi:")
        if COUNTER == 27:
            print("")
            print("Busca Binaria:")

        COUNTER = COUNTER + 1
        timer_test()
