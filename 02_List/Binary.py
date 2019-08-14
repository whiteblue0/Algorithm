def binarySearch(a, key):
    start = 0
    end = len(a)-1
    while start <= end:
        middle = (start + end)//2
        if a[middle] == key:
            return middle
        elif a[middle] > key:
            end = middle -1
        else:
            start = middle +1
    return -1