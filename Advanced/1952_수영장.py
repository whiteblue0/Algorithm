import sys
sys.stdin = open("1952.txt")
import collections


T = int(input())
fee = list(map(int,input().split()))
calander = list(map(int,input().split()))
for _ in range(2):
    calander.append(0)
result = fee[3]
que = collections.deque()
que2 = []
for _ in range(len(calander)):
    que.append(calander[_])

for i in range(3):
    #3달*4, 1년 비교
    cnt = 0

    for j in range(4):
        m3 = calander[i+j*3:i+j*3+3]
        #1달*3, 3달 비교
        tmp = 0
        for _ in range(len(m3)):
            if m3[_]:
                tmp += 1
        if fee[1]*tmp > fee[2]:
            cnt += fee[2]
            continue
        else:
            #1일*일수, 1달 비교
            for k in range(3):
                if m3[k]*fee[0] > fee[1]:
                    cnt += fee[1]
                    continue
                else:
                    cnt += m3[k]*fee[0]
    #1월 비교
    if i == 1:
        if calander[0]*fee[0] > fee[1]:
            cnt += fee[1]
        else:
            cnt += calander[0]*fee[0]
    #1,2월 비교
    elif i == 2:
        if fee[1]*2 > fee[2]:
            cnt += fee[2]
        else:
            if calander[0]*fee[1] > fee[1]:
                cnt += fee[1]
            else:
                cnt += calander[0]*fee[1]
            if calander[1]*fee[1] > fee[1]:
                cnt += fee[1]
            else:
                cnt += calander[1]*fee[1]
    if result > cnt:
        cnt = result
print(result)



