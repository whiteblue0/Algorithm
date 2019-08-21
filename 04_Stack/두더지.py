N = 7
data = [[0,1,1,0,1,0,0],[0,1,1,0,1,0,1],[1,1,1,0,1,0,1],[0,0,0,0,1,1,1],[0,1,0,0,0,0,0],[0,1,1,1,1,1,0],[0,1,1,1,0,0,0]]

cnt = 1
visited = [[0]*N for n in range(N)]

sizelst = []
#우,하,상,좌
dx = [1,0,0,-1]
dy = [0,1,-1,0]


# for i in range(N):
#     print(visited[i])

def ispass(y,x):
    if 0<=y<N and 0<=x<N and data[y][x] ==1 and visited[y][x] ==0:
        return True
    else:
        return False

def DFS(sy,sx):
    visited[sy][sx] = cnt
    stack = [(sy,sx)]
    volume = 0
    while stack:
        y,x = stack.pop()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if ispass(ny,nx):
                stack.append((ny,nx))
                visited[ny][nx] = cnt
                volume += 1
    if volume:
        volume += 1
    sizelst.append(volume)

for i in range(N):
    for j in range(N):
        if ispass(i,j):
            DFS(i,j)
            cnt += 1
if cnt:
    cnt -= 1


for i in range(len(sizelst)-1, 0, -1):
    for j in range(0,i):
        if sizelst[j] > sizelst[j+1]:
            sizelst[j+1], sizelst[j] = sizelst[j], sizelst[j+1]

print(cnt)
for i in range(len(sizelst)-1,-1,-1):
    print(sizelst[i])
