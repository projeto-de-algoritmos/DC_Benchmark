from quick_sort import quick_sort
from list_gen import random_generator, decreasing_generator, growing_generator, equal_generator

import random
import timeit

# Max recursion limit (default: 1000)
import sys
sys.setrecursionlimit(100000)

MAX = 0
COUNTER = 0

RANDOM_LIST = random_generator(1000000)
GROWING_LIST = growing_generator(1000000)
DECREASING_LIST = decreasing_generator(1000000)
EQUAL_LIST = equal_generator(1000000)

def test ():
    """Test function"""
    if COUNTER == 1:
        quick_sort(RANDOM_LIST, 0, MAX)
        print("LISTA ALEATORIA: ")
    if COUNTER == 2:
        quick_sort(GROWING_LIST, 0, MAX)
        print("LISTA CRESCENTE: ")
    if COUNTER == 3:
        quick_sort(DECREASING_LIST, 0, MAX)
        print("LISTA DECRESCENTE: ")
    if COUNTER == 4:
        print("LISTA IDENTICA: ")
        quick_sort(EQUAL_LIST, 0, MAX)

if __name__ == "__main__":
    MAX = int(input()) - 1
    for i in range(0, 4):
        COUNTER = COUNTER + 1
        print(timeit.timeit("test()", setup="from __main__ import test",number = 1))
