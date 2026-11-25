import sys

# Read input
input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
m = int(data[1])
k = int(data[2])
a = int(data[3])
b = int(data[4])

# Calculate the distance in terms of number of subways and floors
subway_distance = abs((a - 1) // (k * m) - (b - 1) // (k * m))
floor_distance = abs((a - 1) % (k * m) - (b - 1) % (k * m))

# Calculate the time for subway and floor travel
subway_time = 10 * subway_distance + subway_distance * (k * m - 1)
floor_time = 5 * floor_distance

# Calculate the total time
total_time = subway_time + floor_time

# Print the result
print(total_time)
