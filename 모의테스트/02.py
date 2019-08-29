import sys
sys.stdin = open('02.txt')

# 상 하 좌 우
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def ispass(x,y):
    return -2000<=x<=2000 and -2000<=y<=2000


T = int(input())
for tc in range(1,T+1):
    N = int(input())    # 1<= N <=1000
    data = [0]*N
    for i in range(N):
        data[i] = list(map(int, input().split()))
    # data[0],data[1] = x,y   K = data[2] = direction   data[3] = energy

    # matrix = [[0]*2000]*2000  다른방법(이따가)
    for i in range(N):
        data[i][1] *= 2
        data[i][0] *= 2

    # for _ in range(N):
    #     print(data[_][0],data[_][1])

    cnt = 0
    while data:

        temp = []
        for i in range(len(data)):
            data[i][1] += dy[data[i][2]]
            data[i][0] += dx[data[i][2]]
            y,x = data[i][1], data[i][0]
            if not ispass(y,x):
                temp.append(i)
        # print(data)

        for i in range(len(temp)-1,-1,-1):
            del data[i]

        temp = []
        for i in range(len(data)):
            y, x = data[i][1], data[i][0]
            if i in temp:
                continue

            else:
                check = []
                check.append(i)
                for j in range(len(data)):
                    if temp:
                        for w in temp:
                            if data[w][1] == data[j][1] and data[w][0] == data[j][0]:
                                temp.append(j)
                                break
                    if i != j and y == data[j][1] and x == data[j][0]:
                        # print('data[j]:',data[j][1],data[j][0])
                        check.append(j)
                if len(check) == 1:
                    check = []
                else:
                    for u in check:
                        temp.append(u)
        temp = set(temp)

        # print('temp:',temp)
        for i in temp:
            cnt += data[i][3]

        # print('cnt:',cnt)


        # for i in range(len(data)):
        #     print(data[i])

        for i in range(len(data)-1,-1,-1):
            if i in temp:
                del data[i]

    print('#{} {}'.format(tc,cnt))