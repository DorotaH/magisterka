import sys
input = sys.stdin.read
data = input().split()
A = [int(x) for x in data]

# Sort the array to minimize the cost
A.sort()

min_cost = sum(A[i] - A[i - 1] for i in range(1, len(A)))
print(min_cost)
