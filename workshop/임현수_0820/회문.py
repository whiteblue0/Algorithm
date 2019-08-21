import sys
sys.stdin = open('회문.txt')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int, input().split())

    table = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            flag = 1
            for k in range(M // 2):
                if table[i][j+M-1-k] != table[i][j+k]:
                    flag = 0
                    break
            if flag:
                ans = [table[i][j+_] for _ in range(M)]


    for j in range(N):
        for i in range(N-M+1):
            flag = 1
            for k in range(M // 2):
                if table[i+M-1-k][j] != table[i+k][j]:
                    flag = 0
                    break
            if flag:
                ans = [table[i+_][j] for _ in range(M)]

    result = ''.join(ans)
    print('#{} {}'.format(tc,result))