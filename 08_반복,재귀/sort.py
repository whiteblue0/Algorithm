arr = [5,2,7,1,3,8,9,3,5,2]

def recurselectionsort(arr,s,e):
    if s == e:
        return
    else:
        mini = s
        for j in range(s+1,e,1):
            if arr[j] < arr[mini]:
                mini = j
        arr[s],arr[mini] = arr[mini], arr[s]
        recurselectionsort(arr,s+1,e)


def selectionsort(arr):
    for i in range(len(arr)):
        mini = i
        for j in range(i+1,len(arr),1):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]

selectionsort(arr)

print(arr)