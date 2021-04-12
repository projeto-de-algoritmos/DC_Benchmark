def merge(arr:list, start:int, middle:int, end:int) -> None:
    """Merge two halves of array in O(n)

            Parameters:
                    arr (list): the main list
                    start (int): the first index
                    middle (int): the middle index
                    end (int): the last index

            Returns:
                    None
    """
    i = start
    j = middle+1
    k = 0

    aux = [0] * len(arr)

    while i <= middle and j <= end:
        if arr[i] <= arr[j]:
            aux[k] = arr[i]
            k+=1
            i+=1
        else:
            aux[k] = arr[j]
            k+=1
            j+=1

    while i <= middle:
        aux[k] = arr[i]
        k+=1
        i+=1
    while j <= end:
        aux[k] = arr[j]
        k+=1
        j+=1

    k = 0
    for i in range(start, end+1):
        arr[i] = aux[k]
        k+=1

def merge_sort(arr, start, end):
    """Sort array in O(nlog(n))

            Parameters:
                    arr (list): the main list
                    start (int): the first index
                    end (int): the last index

            Returns:
                    None
    """
    if start >= end:
        return
    middle = (start + end) // 2
    merge_sort(arr, start, middle)
    merge_sort(arr, middle+1, end)
    merge(arr, start, middle, end)
