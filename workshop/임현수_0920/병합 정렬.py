import sys
sys.stdin = open("merge_input.txt")

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]

        l = merge_sort(left)
        r = merge_sort(right)
        return merge(l,r)
    else:
        return lst

def merge(L,R):
    global cnt
    i = 0
    j = 0
    k = 0
    sorted_lst = [0]*(len(L)+len(R))
    if L[-1] > R[-1]:
        cnt += 1
    while (i < len(L)) and (j < len(R)):
        if L[i] < R[j]:
            sorted_lst[k] = L[i]
            i += 1
            k += 1
        else:
            sorted_lst[k] = R[j]
            j += 1
            k += 1
    while i < len(L):
        sorted_lst[k] = L[i]
        k += 1
        i += 1

    while j < len(R):
        sorted_lst[k]= R[j]
        j += 1
        k += 1

    return sorted_lst


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))
    cnt = 0
    datasort =merge_sort(data)
    n = datasort[N//2]
    print("#{} {} {}".format(tc,n,cnt))