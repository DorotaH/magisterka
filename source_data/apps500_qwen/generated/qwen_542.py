import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Number of items
N = int(data[0])

# Prices of the items
prices = list(map(int, data[1:]))

# Sort the prices in descending order
prices.sort(reverse=True)

# Calculate the total amount to pay
total = prices[0] // 2 + sum(prices[1:])

# Print the total amount
print(total)
