import sys, collections
sys.stdin = open('5658.txt')

def getNum():
    global dataset
    for i in range(4):
        temp = ''
        for j in range(div):
            temp += data[div * i + j]
        temp = int(temp, base=16)
        dataset.add(temp)

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    data = collections.deque()
    for i in input():
        data.append(i)

    div = N//4
    rot = N//4
    dataset = set()
    for i in range(rot):
        num = data.pop()
        data.appendleft(num)
        getNum()
    print("#{} {}".format(tc,sorted(dataset,reverse=True)[K-1]))