arr = [1,2,4,7,8,3]

def babyGin():
    global flag
    check = 0
    if arr[0] == arr[1] and arr[1] == arr[2]:
        check += 1
    if arr[3] == arr[4] and arr[4] == arr[5]:
        check += 1
    if arr[0]+1 == arr[1] and arr[1]+1 == arr[2]:
        check += 1
    if arr[3]+1 == arr[4] and arr[4]+1 == arr[5]:
        check += 1

    if check == 2:
        flag = 1
    return

def permu(c):
    if c == N:
        babyGin()
        return
    else:
        for i in range(N):
           if not visited[i]:
                visited[i] = 1
                result[c] = arr[i]
                permu(c+1)
                visited[i] = 0


N = 6
visited = [0]*N
result = [0]*N

flag = 0

permu(0)
if flag:
    print("babygin")
else:
    print("not babygin")