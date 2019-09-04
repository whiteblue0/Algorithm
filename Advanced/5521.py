import sys
sys.stdin = open('5521.txt')

def bfs(v):


    que = []
    visited[v] = 1
    que.append(v)
    while que:
        v = que.pop(0)
        for w in range(1,N+1):
            if invite[v][w] and not visited[w]:
                visited[w] = visited[v] + 1
                if visited[w] == 3:
                    continue
                que.append(w)



T = int(input())
for tc in range(1,T+1):

    N,M = map(int,input().split())
    visited = [0]*(N+1)
    data = [list(map(int, input().split())) for _ in range(M)]
    invite = [[0]*(N+1) for _ in range(N+1)]
    for i in range(len(data)):
        if data[i][0] != 1:
            result = 0

    for i in range(len(data)):
        invite[data[i][0]][data[i][1]] = 1
        invite[data[i][1]][data[i][0]] = 1

    bfs(1)
    cnt = 0
    for i in range(len(visited)):
        if visited[i] == 2 or visited[i] == 3:
            cnt+=1

    print("#{} {}".format(tc,cnt))

