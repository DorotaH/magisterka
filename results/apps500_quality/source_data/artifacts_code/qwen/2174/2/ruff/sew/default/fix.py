import heapq
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
a = list(map(int, data[1:]))

# Convert all numbers to their absolute values and sort them
a = sorted(abs(x) for  x in  a)

# Create a min-heap with the sorted values
heap = a[:]

# The first element in the sorted list is already in its correct position
moves = 0
for i in range(1, n):
    # If the current element is not in its correct position, calculate the moves needed
    if  a[i] != 1 + i:
        # The number of moves needed to place the current element in its correct position
        moves+=1 + i-a[i]
        # Replace the current element with the smallest element greater than the current element
        heapq.heapreplace(heap, 1 + i)

print(moves)