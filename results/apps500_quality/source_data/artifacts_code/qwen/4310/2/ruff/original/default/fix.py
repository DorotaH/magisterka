import sys

input = sys.stdin.read
data = input().split()
A = list(map(int, data))

# Sort the array to minimize the cost
A.sort()

# The minimum cost is achieved by completing tasks in ascending order
# The cost to complete the i-th task after the (i-1)-th task is |A[i] - A[i-1]|
# Therefore, the total cost is the sum of the absolute differences between consecutive elements
total_cost = 0
for i in range(1, len(A)):
    total_cost += abs(A[i] - A[i-1])

print(total_cost)
