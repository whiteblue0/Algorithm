import sys
sys.stdin = open("2817.txt")

def subset(c,idx,cnt):
    global ans
    if cnt == K:
        ans += 1
        return
    elif cnt > K:
        return

    elif c == N:
        return
    else:
        for i in range(idx,N):
            result[c] = data[i]
            subset(c+1,i+1,cnt + data[i])


T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    data = list(map(int, input().split()))
    visited = [0]*N
    result = [0]*N
    ans = 0

    subset(0,0,0)
    print("#{} {}".format(tc,ans))