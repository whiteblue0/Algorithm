import sys
sys.stdin = open('1244.txt')

T = int(input())
val, K = input().split()
K = int(K)
data = []
for _ in val:
    data.append(int(_))
l = len(data)

stack = []
def swap(a,b,cnt):
    if cnt == K+1:
       return
    stack.append((a,b))
    for i in range(l):
        for j in range(i + 1, l):
            temp = data[:]
            temp[j], temp[i] = temp[i], temp[j]
            swap(i, j, cnt + 1)


swap(0,0,0)
print(stack)