N, M = map(int, input().split())

arr = list(range(1,N+1))

# print(arr)

def comb(M, n, r):
    if M == r:
        print(a)

    elif M-r > N-n :
        return
    else:
        for i in range(r, N):
            a[r] = arr[i]
            comb(M, n+1, r+1)
            comb(M, n+1, r)

a = [0]*M

comb(M, 0, 0)