
def powerset(c,idx,cnt,v):
    global ans

    if cnt > W:
        cnt -= weight[idx-1]
        v -= val[idx-1]
        if ans < v:
            ans = v
        return

    # print(cnt,v)
    if c == N:
        if ans < v:
            ans = v
        return


    for i in range(N):
        if not visited[i]:
            result[c] = i
            visited[i] = 1
            powerset(c+1, i+1, cnt + weight[i],v + val[i])
            visited[i] = 0

W = 10
N = 4
weight = [5,4,6,3]
val = [10,40,30,50]
result = [0]*N
visited = [0]*N
ans = 0

powerset(0,0,0,0)
print(ans)
