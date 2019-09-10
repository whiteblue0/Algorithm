import heapq

heap = [7,2,5,3,4,6]
heapq.heapify(heap)

heapq.heappush(heap,1)
while heap:
    print(heapq.heappop(heap))