def dfs(money,cnt):
    global ans
    if ans < cnt or money < 0:
        return

    if money ==0:
        if ans > cnt:
            ans = cnt
    else:
        for i in range(N):
            dfs(money-coin[i],cnt+1)


data = 730
coin = [10,50,100,500,1250]
M = 730
N = len(coin)

ans = 0x7fffff
dfs(M,0)

print(ans)

