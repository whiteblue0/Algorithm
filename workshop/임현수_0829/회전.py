import sys
sys.stdin = open('회전.txt')

T= int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    line = list(map(int, input().split()))
    trial = M % N
    # print(trial)
    print('#{} {}'.format(tc,line[trial]))