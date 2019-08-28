import sys
sys.stdin = open('im_sample.txt')

T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())

    palate = [[0]*M for _ in range(N)]
    cnt = [0 for _ in range(11)]


    spec = list()
    for i in range(K):
        spec.append(list(map(int, input().split())))
    for i in range(K):
        start  = (spec[i][0],spec[i][1])
        end = (spec[i][2],spec[i][3])
        color = spec[i][4]

        flag = 1
        for i in range(start[0],end[0]+1):
            for j in range(start[1],end[1]+1):
                if palate[i][j] > color:
                    flag = 0
                    break
        if flag:
            for i in range(start[0], end[0]+1):
                for j in range(start[1], end[1]+1):
                    palate[i][j] = color

    for i in range(N):
        for j in range(M):
            cnt[palate[i][j]] += 1


    result = max(cnt)
    print('#{} {}'.format(tc,result))