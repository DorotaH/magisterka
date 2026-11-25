import heapq

n = int(input())
a = list(map(int, input().split()))

# sort elements in descending order
a.sort(reverse=True)

# initialize a priority queue to store the elements
pq = list()
for x in a:
    heapq.heappush(pq, -x)  # use -x to simulate a max heap

# print the elements in the priority queue
for _ in range(n):
    x=-heapq.heappop(pq)
    print(x, end=' ')