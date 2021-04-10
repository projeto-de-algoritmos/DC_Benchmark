from quick_sort import partition, cmpexch
from list_gen import random_generator

def quick_sort_m3(numbers: list, l:int , r: int) -> None:
    if r <= l:
        return

    cmpexch(numbers, (l + r)//2, r)
    cmpexch(numbers, l, (l+r)//2)
    cmpexch(numbers, r, (l+r)//2)

    j = partition(numbers, l, r)
    quick_sort_m3(numbers, l, j-1)
    quick_sort_m3(numbers, j+1, r)