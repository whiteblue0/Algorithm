

T = int(input())

row, col = map(int, input())
arr = [0 for _ in range(col) for _ in range(row)]


for _ in range(row):
    arr.append(list(map(int, input().split())))

arr = [list(map(int, input().split())) for _ in range(row)]


# 델타 배열탐색

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for x in range (len(ary)):
    for y in range(len(ary[x])):
        for i in range(4):
            testX = x + dx[mode]
            testY = y + dx[mode]
            test(ary[testX][testY])
