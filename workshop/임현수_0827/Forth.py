import sys
sys.stdin = open('forth.txt')

T = int(input())

for tc in range(1,T+1):
    order = input().split()

    oper = '+-*/'
    post = []
    stack = []
    for i in range(len(order)-1):
        if order[i] in oper:
            post.append(order[i])
        else:
            post.append(int(order[i]))

    result = 0
    try:
        for i in range(len(post)):

            if post[i] == '+':
                result =stack.pop() + stack.pop()
                stack.append(result)
            elif post[i] == '-':
                a = stack.pop()
                b = stack.pop()
                result = b - a
                stack.append(result)
            elif post[i] == '*':
                result = stack.pop() * stack.pop()
                stack.append(result)
            elif post[i] == '/':
                a = stack.pop()
                b = stack.pop()
                result = b // a
                stack.append(result)
            else:
                stack.append(post[i])
    except IndexError:
        pass


    if len(stack) == 1:
        print('#{} {}'.format(tc,stack[-1]))
    else:
        print('#{} error'.format(tc))