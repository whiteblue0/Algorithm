# input
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1


def iswall(x,y):
    if x < 0 or x >= 5:
        return True
    if y < 0 or y >= 5:
        return True
    return False
def calAbs(y,x):
    if y-x < 0:
        return x-y
    else:
        return y-x

arr = [[0 for _ in  range(5)] for _ in range(5)]

for i in range(5):
    arr[i] = list(map(int, input().split()))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

sum = 0
for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if not iswall(testX, testY):
                sum += calAbs(arr[y][x], arr[testY][testX])
        print(x, y, sum)
print(sum)


ary = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
    for j in range(3):
        if i < j:
            ary[i][j], ary[j][i] = ary[j][i], ary[i][j]

# print(ary)