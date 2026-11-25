import sys

# Read input from standard input
input_str = sys.stdin.read()

# Split input into lines
lines = input_str.strip().split('\n')

# Extract N and K
N, K = map(int, lines[0].split())

# Extract prices
prices = list(map(int, lines[1].split()))

# Sort prices in ascending order
prices.sort()

# Calculate minimum total price
min_price = sum(prices[-K:], 0)

print(min_price)