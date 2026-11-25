import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input values
X = int(data[0])
Y = int(data[1])

# Calculate the cost with the special ticket
discounted_bus_fare = Y / 2
total_cost = discounted_bus_fare + X

# Print the result
print(int(total_cost))
