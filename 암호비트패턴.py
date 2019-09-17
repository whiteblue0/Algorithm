data = '0dec'

asc = ['0000',
       '0001',
       '0011',
       '0100',
       '0101',
       '0110',
       '0111',
       '1000',
       '1001',
       '1010',
       '1011',
       '1100',
       '1101',
       '1110',
       '1111']

def aToh(c):
    if c <= '9':
        return  ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

def makeT(x):
    for i in range(4):
        t.append(asc[x][i])

t = []

arr = '0dec'
for i in range(len(arr)):
    makeT(aToh(arr[i]))

n = 0
for i in range(len(t)):
    n = n*2 + t[i]
    if i % 7 == 0:
        print(n,end=", ")
        n=0
if i%7 !=6:
    print(n)