# 조합
def combi1(c, idx):
    if c == K:
        print(result)
        return

    for i in range(idx, N):
        result[c] = i
        combi1(c + 1, i + 1)

# N개 중 K개 뽑는 경우의 수
N = 5
K = 3
data = [1, 2, 3, 4, 5]
result = [0] * K
# combi1(0, 0)




# 순열
def permu1(c):
    print(result[:c])
    if c == K:
        # print(result)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            result[c] = data[i]
            permu1(c+1)
            visited[i]=0




N = 5
K = 5
data = [1,2,3,4,5,6]
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
K = 5
data = [1,2,3,4,5]
result = [0]*K
# permu2(0)





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
    #부분집합
    print(result[:c])

    if c== N:
        #조합
        return

    for i in range(idx,N):
        result[c] = data[i]
        subset(c+1,i+1)

N = 4
data = [1,2,3,4]
result = [0]*N
subset(0,0)
