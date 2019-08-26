

data = ['2','+','3','*','4','/','5']
fixlst = []
stack = []

for i in range(len(data)):
    if data[i] == '+' or data[i] == '-' or data[i] == '*' or data[i] == '/':
        stack.append(data[i])
    else:
        print(data[i],end='')

while len(stack):
    print(stack.pop(),end='')