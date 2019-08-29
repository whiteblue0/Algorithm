import sys
sys.stdin = open('피자 굽기.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    cheese = list(map(int,input().split()))
    pizza = []
    for i in range(len(cheese)):
        pizza.append([i+1,cheese[i]])
    # pizza[0]: pizza num , pizza[1]: cheese volume, pizza[2]:count
    # print(pizza)
    que = [[0,0] for _ in range(N)]

    for i in range(N):
        que[i] = pizza.pop(0)


    # print(pizza)

    flag = 1
    cnt = 0
    while flag:
        if cnt == N:
            for i in range(N):
                que[i][1] //= 2
        cnt %= N
        #
        # print('남은피자',pizza)
        # print('구운피자:', que[0])
        if que[0][1] == 0:
            done = que.pop(0)
            # print('done:',done)
            if pizza:
                que.insert(0, pizza.pop(0))
            else:
                que.insert(0, [0,0])
        temp = 0
        for w in range(len(que)):
            temp += que[w][0] + que[w][1]
        if temp == 0:
            flag = 0


        # for _ in range(N):
        #     print(_,que[_])
        # print()
        rot = que.pop(0)
        que.append(rot)
        cnt += 1






    print('#{} {}'.format(tc,done[0]))