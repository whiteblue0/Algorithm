import sys
sys.stdin = open('문자열 비교.txt')

T = int(input())

for tc in range(1,T+1):
    target = input()
    table = input()
    l1 = len(target)
    l2 = len(table)

    cnt = 0
    for i in range(l2-l1+1):
        flag = 1
        for j in range(l1):
            if table[i+j] != target[j]:
                flag = 0
                break
        if flag:
            cnt = 1

    print('#{} {}'.format(tc,cnt))