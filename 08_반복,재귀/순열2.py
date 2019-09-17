def perm(n,r,q):
    if r ==0:
        for i2 in range(q-1,-1,-1):
            print("%d " % t[i2], end="")
        print()
    else:
        for i in range(n-1,-1,-1):
            arr[i], arr[n-1] = arr[n-1], arr[i]
            t[r-1] = arr[n-1]
            perm(n-1,r-1,q)
            arr[i], arr[n-1] = arr[n-1], arr[i]


arr =[1,2,3,4]
t = [0]*3

perm(4,2,3)