def exch(numbers: list, a: int, b: int) -> None:
    """Exchange the values of numbers at a and b.

            Parameters:
                    numbers (list): the main list
                    a (int): the first index
                    b (int): the second index

            Returns:
                    None
    """
    temp = numbers[a]
    numbers[a] = numbers[b]
    numbers[b] = temp

def cmpexch(numbers: list, a: int, b: int) -> None:
    """Exchange the values of numbers at a and b
    if the number at a is bigger than the number
    at b.

            Parameters:
                    numbers (list): the main list
                    a (int): the first index
                    b (int): the second index

            Returns:
                    None
    """
    if numbers[b] < numbers[a]:
        exch(numbers, a, b)

def partition(numbers: list, l: int, r: int) -> int:
    """Partition array around last element (pivot).
    Places all smaller (smaller than pivot) to left
    of pivot and all greater to right of pivot.

            Parameters:
                    numbers (list): the main list
                    l (int): most left of the list
                    r (int): most right of the list

            Returns:
                Middle element
    """
    c = numbers[r]
    j = l

    k = l
    while k < r:
        if numbers[k] < c:
            exch(numbers, k, j)
            j = j + 1
        k = k + 1
    exch(numbers, j, r)
    return j

def quick_sort(numbers: list, l:int , r: int) -> None:
    """Divide and Conquer sort algorithm. Partition
    elements until

            Parameters:
                    numbers (list): the main list
                    l (int): most left of the list
                    r (int): most right of the list

            Returns:
                    None
    """
    if len(numbers) == 1:
        return
    if l < r:
        j = partition(numbers, l, r)
        quick_sort(numbers, l, j-1)
        quick_sort(numbers, j + 1, r)

