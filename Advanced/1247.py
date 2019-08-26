#순열
def getD(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def calc():
    global ans
    dist = 0
    for i in range(N-1):
        dist += getD(target[A[i]],target[A[i+1]])
    dist += getD(company,target[A[0]])
    dist += getD(target[A[N-1]], home)

    if ans > dist:
        ans = dist

def perm(n, k):
    if n == k:
        calc()
    else:
        for i in range(k, n):
            A[i], A[k] = A[k],A[i]
            perm(n,k+1)
            k, i = i, k

import sys
sys.stdin = open('(1247)최적경로_input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    temp = list(map(int, input().split()))
    A = list(range(N))
    ans = 987654321

    company = (temp[0],temp[1])
    home = (temp[2],temp[3])
    target = []

    for i in range(4,len(temp),2):
        target.append((temp[i],temp[i+1]))


    perm(N,0)
    print('#{} {}'.format(tc,ans))



