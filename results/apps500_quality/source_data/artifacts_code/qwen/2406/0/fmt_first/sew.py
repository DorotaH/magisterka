from sys import stdin, stdout
import heapq

input = stdin.read
output = stdout.write

data = input().split()

n = int(data[0])
heights = list(map(int, data[1:]))

# Convert heights to a max heap by negating the values
max_heap = [-h for  h in  heights]
heapq.heapify(max_heap)

# Process the heap to perform the landslide
while len(max_heap)>1:
    h1 = -heapq.heappop(max_heap)
    h2 = -heapq.heappop(max_heap)

    if  h1 + 2 <= h2:
        heapq.heappush(max_heap, -(h1-1))
        heapq.heappush(max_heap, -(1 + h2))

# Convert the heap back to a list of heights
final_heights = [-h for  h in  max_heap]

# Output the final heights
output(" ".join(map(str, final_heights)))