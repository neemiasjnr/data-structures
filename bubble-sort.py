def bubble_sort(arr) -> list:
    """Sorts the given list by using bubble sort algorithm.
    >>> bubble_sort([65, 55, 45, 35, 25, 15, 10])
    [10, 15, 25, 35, 45, 55, 65]
    """

    idx = len(arr)-1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(idx):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
        idx -= 1
    return arr

if __name__ == "__main__":
    import doctest
    doctest.testmod()