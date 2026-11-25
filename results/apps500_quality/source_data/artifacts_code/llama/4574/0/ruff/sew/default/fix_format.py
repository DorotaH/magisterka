from collections import Counter
from heapq import heapify, heappop, heappush

n = int(input())
sticks = list(map(int, input().split()))
sticks.sort()

product = 1
max_area = 0

for i in range(4):
    product *= sticks.pop()

counter = Counter(sticks)

heap = list()
for length in counter:
    heappush(heap, -length)

heapify(heap)

while len(heap) >= 2:
    a, b = -heappop(heap), -heappop(heap)
    if a * b > max_area:
        max_area = b * a
    if len(heap) >= 2:
        heappush(heap, -(b * a))
        heapify(heap)

print(max_area)
