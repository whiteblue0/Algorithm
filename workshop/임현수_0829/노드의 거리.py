import sys
sys.stdin = open('노드의 거리.txt')

def BFS(v):
    que = []
    que.append(v)
    visited[v] = 1
    while que:
        v = que.pop(0)
        if v == cx:
            return visited[v]-1
        for w in range(1,V+1):
            if portal[v][w] and not visited[w]:
                que.append(w)
                visited[w] = visited[v] + 1
    if not visited[cx]:
        return 0

T = int(input())
for tc in range(1,T+1):
    V,E = map(int, input().split())

    portal = [[0]*(V+1) for _ in range(V+1)]

    visited = [0]*(V+1)

    for i in range(E):
        start, end = map(int, input().split())
        portal[start][end] = 1
        portal[end][start] = 1

    cy,cx = map(int,input().split())

    d = BFS(cy)
    print('#{} {}'.format(tc,d))