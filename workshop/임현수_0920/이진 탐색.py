import sys
sys.stdin = open("이진탐색.txt")

def binarySearch(nlst,k):
    global flag,cnt

    if len(nlst):
        l = 0
        r = len(nlst) - 1
        m = (l + r) // 2

        if nlst[m] == k:
            cnt += 1
            return
        elif nlst[m] < k:
            if flag == 1:
                return
            flag = 1
            binarySearch(nlst[m+1:r+1],k)
        elif nlst[m] > k:
            if flag == 2:
                return
            flag = 2
            binarySearch(nlst[:m],k)

T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    nlst = list(map(int,input().split()))
    nlst.sort()
    mlst = list(map(int,input().split()))
    cnt = 0
    for i in mlst:
        flag = None
        binarySearch(nlst,i)

    print("#{} {}".format(tc,cnt))