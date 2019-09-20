import sys
sys.stdin = open("퀵정렬.txt")

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

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = list(map(int, input().split()))
    quick_sort(data,0,N-1)
    print("#{} {}".format(tc,data[N//2]))