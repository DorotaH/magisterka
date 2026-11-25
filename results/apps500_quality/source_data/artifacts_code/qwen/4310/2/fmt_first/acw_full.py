import sys

input = sys.stdin.read
data = input().split()
A = list(map(int, data))

# Sort the array to minimize the cost
A.sort()

total_cost = sum(abs(A[i] - A[i - 1]) for i in range(1, len(A)))
print(total_cost)
