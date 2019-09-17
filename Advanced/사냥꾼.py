import sys
sys.stdin = open("사냥꾼.txt")
# 0 : 빈 공간, 1 : 사냥꾼, 2 : 토끼, 3: 바위

# 상 우상 우 우하 하 좌하 좌 좌상
dx = [ 0, 1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1, 1, 0,-1]

def ispass(y,x):
    return 0<=y<N and 0<=x<N and data[y][x] != 3


T = int(input())
for tc in range(1,T+1):
    N = int(input())

    data = [list(map(int,input().split())) for _ in range(N)]
    #
    # for _ in range(N):
    #     print(data[_])
    # print()

    cnt = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                # print("i,j:",i,j)
                for d in range(8):
                    ny,nx = i+dy[d],j+dx[d]
                    while ispass(ny,nx):
                        if data[ny][nx] == 2:
                            cnt += 1
                        ny += dy[d]
                        nx += dx[d]

    print("#{} {}".format(tc,cnt))