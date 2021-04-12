def binary_search(arr, start, end, x):
    """Search x in arr

        Parameters:
            arr (int): vector of integers
            start/end (int): range of search
            x (int): searched element

        Returns:
            x is in arr: index of x
            else: -1
    """
    if end < start:
        return -1

    mid = (start + end) // 2

    if x == arr[mid]:
        return mid
    elif x < arr[mid]:
        return binary_search(arr, start, mid-1, x)
    else:
        return binary_search(arr, mid+1, end, x)
