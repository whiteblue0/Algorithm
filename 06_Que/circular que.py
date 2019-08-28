# define circular Que
def isfull():
    if (rear+1) % len(que) == front:
        return True
    else:
        return False
def isempty():
    if front == rear:
        return True
    else:
        return False
def full():
    if rear == len(que) -1:
        return True
    else:
        return False

def enque(item):
    global rear
    if isfull():
        print('queue_full')
    else:
        rear += 1
        rear %= len(que)
        que[rear] = item
def  deque():
    global front
    if isempty():
        print('queue_empty')
    else:
        front += 1
        front %= len(que)
        return que(front)
def qpeek():
    global front, rear
    if isempty():
        print('queue_empty')
    else:
        return que[front+1]

SIZE = 100
que = [0]*SIZE

front , rear = -1, -1