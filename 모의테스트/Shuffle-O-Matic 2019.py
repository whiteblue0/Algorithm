import sys
from copy import deepcopy
sys.stdin = open('shuffle.txt')

T = int(input())
# for tc in range(1,T+1):
N = int(input())

deck = list(map(int,input().split()))

shuffle = deepcopy(deck)
sol = sorted(deck)
Ldeck = shuffle[:len(shuffle)//2]
Rdeck = shuffle[len(shuffle)//2:]

que = []
for x in range(N-1):
    while len(Rdeck) > x:
        que.append(1)
    for k in range(x):




rev = list(reversed(deck))


