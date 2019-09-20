def partition(A, l, r):
   p = A[l]
   i = l
   j = r
   while i < j:
       while i < r and A[i] <= p:
           i += 1
       while j > l and A[j] >= p:
           j -= 1
       if i < j :
           A[i], A[j] = A[j], A[i]
   A[l], A[j] = A[j], A[l]
   return j
def quick_sort(A, l, r):
   if l < r:
       s = partition(A, l, r)
       quick_sort(A, l, s - 1)
       quick_sort(A, s + 1, r)


arr = [3, 5, 1, 2, 9, 6, 4, 7, 5]
quick_sort(arr,0,len(arr)-1)
print(arr)