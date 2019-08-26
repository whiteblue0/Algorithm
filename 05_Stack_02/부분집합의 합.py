cnt = 0
total = 0
N = 10
A = [0 for _ in range(N)]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def printSet(n,setsum):
    global cnt


    if setsum == 10:
        cnt += 1
        print("%d : " % cnt, end='')
        for i in range(n):
            if A[i] == 1:
                print("%d " % data[i], end='')
    print()

def powerSet(n, k, setsum):
    global total
    total += 1

    if setsum > 10:
        return
    if n == k:
        printSet(n,setsum)
    else:
        A[k] = 1
        powerSet(n, k + 1, setsum + data[k])
        A[k] = 0
        powerSet(n, k + 1, setsum)


powerSet(N, 0, 0)
print('함수호출 횟수: {}'.format(total))
