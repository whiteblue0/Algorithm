cnt = 0
N = 3
A = [0 for _ in range(N)]
data = [1,2,3,4,5,6,7,8,9,10]

def printSet(n):
    global cnt
    cnt += 1


    print("%d : " % (cnt),end='')
    for i in range(n):
        if A[i] == 1:
            print("%d " % (data[i]),end='')
    print()


def powerSet(n, k):
    if n == k:
        printSet(n)
    else:
        A[k] = 1
        powerSet(n,k+1)
        A[k] = 0
        powerSet(n,k+1)

powerSet(N,0)


