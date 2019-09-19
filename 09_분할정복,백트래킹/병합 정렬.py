import sys
sys.stdin = open("병합정렬.txt")

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
    i = 0
    j = 0
    sorted_lst = []
    while (i < len(L)) & (j < len(R)):
        if L[i] < R[j]:
            sorted_lst.append(L[i])
            i += 1
        else:
            sorted_lst.append(R[j])
            j += 1
    while i < len(L):
        sorted_lst.append(L[j])
        i += 1

    while j < len(R):
        sorted_lst.append(R[j])
        j += 1

    return sorted_lst


T = int(input())
N = int(input())
data = list(map(int,input().split()))

print(merge_sort(data))