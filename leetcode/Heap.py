import heapq

#Min-Heap
min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 4)
print(min_heap)

print(heapq.heappop(min_heap)) # remove o menor elemento
print(min_heap)

# Max_heap
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -4)
print(max_heap)

print(-heapq.heappop(max_heap))
