def comb(n,r,q):
    if r == 0:
        for i2 in range(q):
            print("{}".format(T[i2]),end="")
        print()
    elif n < r:
        return
    else:
        T[r-1] = arr[n-1]
        comb(n-1,r-1,q)
        comb(n-1,r,q)

arr = [1,2,3,4]
T = [0]*3

comb(4,3,3)