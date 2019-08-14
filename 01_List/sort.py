def BubbleSort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


data = [55, 7, 78, 12, 42]
print(data)
BubbleSort(data)
print(data)

def CountingSort(A,B,k):
    #A[1...n] 입력리스트 사용된 숫자(1~k)
    #B[1...n] 정렬된 리스트
    #C[1...n] 카운트 리스트
    
    C = [0]*k
    for i in range(0, len(B)):
        C[A[i]] += 1
    for i in range(1,len(C)):
        C[i] += C[i-1]
    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1