#순열
def getD(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def calc():
    global ans
    dist = 0
    for i in range(N-1):
        dist += getD(target[A[i]],target[A[i+1]])
    dist += getD(company,target[A[0]])
    dist += getD(company[A[N-1]], home)

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
sys.stdin = open('1247.txt')

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


# for tc in range(1,T+1):
#     N = int(input())
#
#     raw = list(map(int, input().split()))
#
#     startpoint = [0, 0]
#     for _ in range(2):
#         startpoint[_] = raw.pop(0)
#     for _ in range(2):
#         raw.append(raw.pop(0))
#     targetlst = []
#
#     for i in range(len(raw)//2):
#         targetlst.append((raw[2*i], raw[2*i+1]))
#
#     cnt = 0
#     position = startpoint
#
#     while targetlst:
#         # print(position)
#         housenum = len(targetlst)
#         short = 200
#         shortidx = 0
#         for i in range(housenum):
#             temp = abs(targetlst[i][0]-position[0])+abs(targetlst[i][1]-position[1])
#             if short > temp:
#                 short = temp
#                 shortidx = i
#         cnt += short
#         position = targetlst.pop(shortidx)
#
#     print('#{} {}'.format(tc,cnt))

