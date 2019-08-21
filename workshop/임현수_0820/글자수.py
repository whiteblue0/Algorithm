import sys
sys.stdin = open('글자수.txt')

T = int(input())

for tc in range(1,T+1):
    strN = input()
    N = len(strN)

    strM = input()
    M = len(strM)

    wmax = 0
    for i in range(N):
        cnt = 0
        for j in range(M):

            if strN[i] == strM[j]:
                cnt += 1
        if wmax <= cnt:
            wmax = cnt

    print('#{} {}'.format(tc, wmax))