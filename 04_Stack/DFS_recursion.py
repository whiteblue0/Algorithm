# def DFS_recursion(G,v):
#     visited[v] = True
#     for each all w in adjacency(G, v)
#     if visited[w] != True:
#         DFS_recursion(G, v)

import sys
sys.stdin = open('dfs.txt')


stack = []
def DFS(n):
    visited[n] = 1
    print(n, end= ' ')

    for i in range(V+1):
        if G[n][i] == 1 and visited[i] == 0:

            DFS(i)


V, E = map(int, input().split())

temp = list(map(int,input().split()))

G = [[0 for _ in range(V+1)] for a in range(V+1)]
visited = [0 for i in range(V+1)]

for i in range(0, len(temp),2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

for i in range(V+1):
    print('{} {}'.format(i,G[i]))

DFS(1)
