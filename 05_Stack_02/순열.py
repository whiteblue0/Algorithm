def PrintArr(n):
    for i in range(n):
        print(arr[i],end=" ")


def perm(n, k):
    if n == k:
        print(arr)
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k],arr[i]
            perm(n,k+1)
            arr[k], arr[i] = arr[i], arr[k]

arr = [1,2,3] #data
perm(3, 0)