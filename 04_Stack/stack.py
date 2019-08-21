def push(data):
    stack.append(data)

def stackpop():
    if not len(stack):
        return
    else:
        return stack.pop()

stack = []

# for i in range(1,4):
#     push(i)
#
# print(stack)
# for i in range(len(stack)):
#     print(stackpop())

'''
input:
()()((()))
((()((((()()((()())((())))))
'''

def check_matching(data):
    cnt = 0
    for i in range(len(data)):
        stack.append(data[i])
    while stack:
        check = stack.pop()
        if check == '(':
            cnt += 1
        else:
            cnt -= 1

    if cnt == 0:
        return True
    else:
        return False

data = input()

print(check_matching(data))
