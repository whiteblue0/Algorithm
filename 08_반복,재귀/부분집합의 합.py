
def powerset(c,idx,cnt):

    if cnt == 10:
        print(result[:c])

    elif cnt > 10:
        return
    elif c == N:
        return
    else:
        for i in range(idx,N):
            visited[i] = 1
            result[c] = data[i]
            powerset(c+1,i+1,cnt+ data[i])
            visited[i] = 0


data = [1,2,3,4,5,6,7,8,9,10]
N = len(data)
result = [0]*N
visited = [0]*N

powerset(0,0,0)