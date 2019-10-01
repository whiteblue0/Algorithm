

coin = [0,1,5,10,16]
N = len(coin)
M = 20
table = [[0]*(M+1) for _ in range(len(coin))]
for i in range(M+1):
    table[0][i] = 0x7ffffff

for i in range(1,5):
    for j in range(1,21):
        if j < coin[i]:
            table[i][j] = table[i-1][j]
        else:
            table[i][j] = min(table[i][j-coin[i]] + 1, table[i-1][j])

for i in range(1,5):
    for j in range(1,21):
        print("{} ".format(table[i][j]),end="")
    print()

print("{} coins".format(table[4][20]))