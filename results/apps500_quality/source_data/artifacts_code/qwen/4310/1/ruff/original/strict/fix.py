import sys

input = sys.stdin.read
data = input().split()
A = [int(x) for x in data]

# Sort the array to minimize the cost
A.sort()

# The minimum cost is the sum of the differences between consecutive elements
min_cost = 0
for i in range(1, len(A)):
    min_cost += A[i] - A[i-1]

print(min_cost)
