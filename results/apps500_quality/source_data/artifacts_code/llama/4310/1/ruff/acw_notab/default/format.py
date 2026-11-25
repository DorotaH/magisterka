import sys

# Read input from standard input
A = list(map(int, input().split()))

# Initialize a list to store the minimum cost for each task
min_costs = [0] * len(A)

# Calculate the minimum cost for each task
for i in range(len(A)):
    min_costs[i] = min((A[i] - A[j]) ** 2 for j in range(len(A)) if j != i)

# Print the minimum total cost
print(sum(min_costs))
