import sys
sys.stdin = open("전기버스.txt")

def dfs(c,cnt):
    global result

    if cnt >= result:
        return

    if c >= N-1:
        if result > cnt:
            result = cnt
        return

    for i in range(1,data[c]+1):
        dfs(c+i,cnt+1)

T = int(input())
for tc in range(1,T+1):
    temp = list(map(int, input().split()))
    N = temp[0]
    data = [0]*(N)
    for _ in range(len(temp)-1):
        data[_] = temp[_+1]

    result = 987654321
    dfs(0,0)
    result -= 1
    print("#{} {}".format(tc,result))