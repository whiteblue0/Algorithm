# 조합
def combi1(c, idx):
    if c == K:
        print(result)
        return

    for i in range(idx, N):
        result[c] = i
        combi1(c + 1, i + 1)


N = 5
K = 3
data = [1, 2, 3, 4, 5]
result = [0] * K
# combi1(0, 0)




# 순열
def permu1(c):
    if c == K:
        print(result)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            result[c] = i
            permu1(c+1)
            visited[i]=0




N = 5
K = 3
data = [1,2,3,4,5]
visited = [0]*N
result = [0]*K

# permu1(0)




# 중복 순열
def permu2(c):
    if c == K:
        print(result)
        return

    for i in range(N):
        result[c] = i
        permu2(c+1)
N = 5
K = 3
data = [1,2,3,4,5]
result = [0]*K
# permu2(10)





# 중복 조합
def combi2(c,idx):
    if c == K:
        print(result)
        return

    for i in range(idx,N):
        result[c] = i
        combi2(c+1,i)
N = 5
K = 3
data = [1,2,3,4,5]
result = [0]*K
# combi2(0,0)




# 부분집합
def subset(c,idx):
    print(result[:c])

    if c==N:
        return

    for i in range(idx,N):
        result[c] = data[i]
        subset(c+1,i+1)

N = 4
data = [2,3,4,5]
result = [0]*N
subset(0,0)
