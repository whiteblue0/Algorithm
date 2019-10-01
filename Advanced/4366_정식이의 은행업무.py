import sys
sys.stdin = open("4366.txt")

T = int(input())
for tc in range(1,T+1):
    Nst = input()
    Nrd = input()
    result = 0
    table = []
    binchecker = []

    for t in Nst:
        binchecker.append(t)
    for j in range(len(binchecker)):
        if binchecker[j] == '1':
            binchecker[j] = '0'
            table.append(int(''.join(binchecker),2))
            binchecker[j] = '1'
        else:
            binchecker[j] = '1'
            table.append(int(''.join(binchecker),2))
            binchecker[j] = '0'

    thrdchecker = []
    for t in Nrd:
        thrdchecker.append(t)
    for j in range(len(thrdchecker)):
        if thrdchecker[j] == '0':
            thrdchecker[j] = '1'

            tmp = int(''.join(thrdchecker), 3)
            if tmp in table:
                result = tmp
                break

            thrdchecker[j] = '2'
            tmp = int(''.join(thrdchecker), 3)
            if tmp in table:
                result = tmp
                break
            thrdchecker[j] = '0'

        elif thrdchecker[j] == '1':
            thrdchecker[j] = '0'
            tmp = int(''.join(thrdchecker), 3)
            if tmp in table:
                result = tmp

            thrdchecker[j] = '2'
            tmp = int(''.join(thrdchecker), 3)
            if tmp in table:
                result = tmp
                break
            thrdchecker[j] = '1'

        elif thrdchecker[j] == '2':
            thrdchecker[j] = '0'
            tmp = int(''.join(thrdchecker), 3)
            if tmp in table:
                result = tmp
                break

            thrdchecker[j] = '1'
            tmp = int(''.join(thrdchecker), 3)
            if tmp in table:
                result = tmp
                break
            thrdchecker[j] = '2'

    print("#{} {}".format(tc,result))
