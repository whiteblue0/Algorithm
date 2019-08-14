import sys
sys.stdin = open('snail.txt')

T = int(input())

def ispass(y,x):
    return 0<=y<N and 0<=x<N and not data[y][x]

#우>하>좌>상
dy = [0,1,0,-1]
dx = [1,0,-1,0]
for a in range(1,T+1):
    N = int(input())

    y,x,d = 0,0,0
    data = [[0]*N for _ in range(N)]

    for i in range(N**2):
        data[y][x] = i+1
        ny = y + dy[d]
        nx = x + dx[d]
        if not ispass(ny, nx):
            d += 1
            d %= 4
            ny = y + dy[d]
            nx = x + dx[d]
        y = ny
        x = nx

    print('#{}'.format(a))
    for j in range(N):
        for i in range(N):
            print(data[j][i], end=' ')
        print('')