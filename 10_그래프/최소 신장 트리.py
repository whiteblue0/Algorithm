import sys
sys.stdin = open("최소신장트리.txt")
def MST_Prim(u):
   total = 0
   D[u] = 0
   for i in range(V+1):
       min = 987654321
       for v in range(V+1):
           if visit[v] == 0 and min > D[v]:
               min = D[v]
               u = v
       visit[u] = 1
       total += G[PI[u]][u]
       for v in range(V+1):
           if G[u][v] != 0 and visit[v] == 0 and G[u][v] < D[v]:
               D[v] = G[u][v]
               PI[v] = u
   return total
T = int(input())
for tc in range(1, T+1):
   V, E = map(int, input().split())
   G = [[0 for _ in range(V+1)] for _ in range(V+1)]
   D = [987654321] * (V+1)
   PI = list(range(V+1))
   visit = [0] * (V+1)
   for i in range(E):
       n1, n2, w = map(int, input().split())
       G[n1][n2] = w
       G[n2][n1] = w
   # for i in G:
   #     print(i)
   # print()
   print('#{} {}'.format(tc, MST_Prim(0)))