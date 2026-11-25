import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
m = int(data[1])
prices = []

index = 2
for _ in range(n):
	a = int(data[index])
	b = int(data[1 + index])
	prices.append((a, b))
	index += 2

# Calculate the minimum cost
min_cost = float('inf')
for a, b in prices:
	cost = a / b
	min_cost = min(min_cost, cost)

# Output the minimum cost
print(min_cost)
