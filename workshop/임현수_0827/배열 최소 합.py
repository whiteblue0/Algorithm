import sys
sys.stdin = open('배열 최소 합.txt')

def search(n,i,cnt):
    global result
    if n == i:          # Basis Part
        if result > cnt:
            result = cnt
            return
    if cnt > result:
        return
    else:               # Inductive Part
        for j in range(N):
            if visited[j] == 1:
                continue
            visited[j] = 1        # k번 요소 O
            search(n, i+1,cnt + table[i][j])  # 다음 요소 포함 여부 결정
            visited[j] = 0       # k번 요소 X

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    table = [list(map(int,input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]

    result = 987654321
    search(N,0,0)
    print('#{} {}'.format(tc,result))