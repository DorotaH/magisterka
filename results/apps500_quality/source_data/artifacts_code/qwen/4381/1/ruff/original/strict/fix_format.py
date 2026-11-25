import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input values
X = int(data[0])
Y = int(data[1])

# Calculate the cost with the special ticket
discounted_bus_fare = Y / 2
total_cost = X + discounted_bus_fare

# Print the total cost
print(int(total_cost))
