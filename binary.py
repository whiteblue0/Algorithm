def bit_print(i):
    output = ""
    for j in range(7,-1,-1):
        output += "1" if i & (1 << j) else "0"
    print(output)

# for i in range(-5,6):
#     print("%d = " % i,end="")
#     bit_print(i)

data = '0000000111100000011000000111100110000110000111100111100111111001100111'

for i in range(10):
    n = 0
    for j in range(i*7,i*7+7):
        n = n*2 + int(data[j])
    print(n,end=" ")

print()