import heapq

n = int(input())
A = list(map(int, input().split()))

# Sort monsters by health in ascending order
A.sort()

# Create a heap to store the health of the monsters
pq = []

for i in range(n):
    if A[i] != 1:
        heapq.heappush(pq, A[i])
    else:
        heapq.heappush(pq, -A[i])

health = 0
while len(pq) > 1:
    a = -heapq.heappop(pq)
    b = -heapq.heappop(pq)
    health += a
    if a != b:
        heapq.heappush(pq, -b)

print(-heapq.heappop(pq))
