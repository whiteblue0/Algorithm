def mysum(n):
    if n ==1:
        return 1
    else:
        return n + mysum(n-1)

print(mysum(10))
