import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
N, prices = int(data[0]), list(map(int, data[1:]))

# Find the index of the item with the highest price
max_index = prices.index(max(prices))

# Calculate the total amount with the discount
total_amount = sum(prices, 0) - (prices[max_index] / 2)

# Print the total amount
print(total_amount)
