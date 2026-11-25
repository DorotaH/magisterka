import heapq

N = int(input())
A = list(map(int, input().split()))
heap = []

for i, a in enumerate(A, start=1):
	if a > 1:
		heapq.heappush(heap, (a, i))

while 1 < len(heap):
	a, i = heapq.heappop(heap)
	if a >= heap[0][0]:
		heapq.heappush(heap, (a + heap[0][0], i))
		heapq.heappop(heap)
	else:
		heapq.heappush(heap, (a, i))

print(heap[0][0])
