from collections import Counter
from heapq import heapify, heappop, heappush

n = int(input())
sticks = list(map(int, input().split()))
sticks.sort()

product = 1
max_area = 0

for _ in range(4):
	product *= sticks.pop()

counter = Counter(sticks)

heap = []
for length in counter:
	heappush(heap, -length)

heapify(heap)

while 2 <= len(heap):
	a = -heappop(heap)
	b = -heappop(heap)
	max_area = max(max_area, a * b)
	if 2 <= len(heap):
		heappush(heap, -(a * b))
		heapify(heap)

print(max_area)
