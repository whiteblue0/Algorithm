def BFS(v):
    que = []
    que.append(v)
    visited[v] = 1
    print(v, end= ' ')
    while que:
        v = que.pop(0)
        for w in range(1,V+1):
            if G[v][w] and not visited[w]:
                que.append(w)
                visited[w] = visited[v] + 1
                print(w, end=' ')

data = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
V, E = 7, 8

G = [[0]*(V+1) for _2 in range(V+1)]
visited = [0]*(V+1)

for i in range(E):
    start = data[i*2]
    end = data[i*2+1]
    G[start][end] = 1

for i in range(len(G)):
    print(i,G[i])

BFS(1)
print(visited)