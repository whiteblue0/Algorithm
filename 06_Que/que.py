
# define Que
def isfull():
    if rear ==len(que)-1:
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

# python Que
que = []
que.append(1)
que.append(2)
que.append(3)

print(que.pop(0))
print(que.pop(0))
print(que.pop(0))

# Queue Library
import queue
q = queue.Queue()

q.put(1)
q.put(2)
q.put(3)

print(q.get())
print(q.get())
print(q.get())