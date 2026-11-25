import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
N = int(data[0])
K, p = int(data[1]), list(map(int, data[2:]))

# Sort the prices in ascending order
p.sort()

# Calculate the minimum possible total price
min_price = sum(p[:K], 0)

# Print the result
print(min_price)
