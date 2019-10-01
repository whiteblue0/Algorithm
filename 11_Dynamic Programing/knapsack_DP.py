W = 10
N = 4
weight = [0,5,4,6,3]
value = [0,10,40,30,50]

K = [[0]*(sum(weight)) for _ in range(sum(value))]

for i in range(1,N+1):
    for w in range(1,W+1):
        if weight[i] > w:
            K[i][w] = K[i-1][w]
        else:
            K[i][w] = max(K[i-1][w-weight[i]] + value[i], K[i-1][w])

for i in range(N+1):
    for w in range(W+1):
        print("{} ".format(K[i][w]),end="")
    print()
