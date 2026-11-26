import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Convert input data to integers
A, B = int(data[0]), int(data[1])
C, D = int(data[2]), int(data[3])
E = int(data[4])

# Calculate the earliest possible time for the last dish to be delivered
# by ordering the dishes in ascending order of their delivery times
delivery_times = sorted([A, B, C, D, E])
last_delivery_time = sum(delivery_times, 0)

# Print the result
print(last_delivery_time)
