#1. fibonach
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

# print(fibo(8))

#memorize

def newfibo(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(newfibo(n-1) + newfibo(n-2))
    return memo[n]

memo = [0, 1]

# print(newfibo(7))

def fibo2(n):
    f = [0, 1]
    print(f)
    for i in range(2, n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]

print(fibo2(1000))