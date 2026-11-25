import sys

# Read input
input = sys.stdin.read
data = input().split()

# Parse input
n, m = int(data[0]), int(data[1])
k, a = int(data[2]), int(data[3])
b = int(data[4])

# Calculate the distance in terms of number of subways and floors
subway_distance, floor_distance = abs((a - 1) // (m * k) - (b - 1) // (m * k)), abs((a - 1) % (m * k) - (b - 1) % (m * k))

# Calculate the time for subway and floor travel
subway_time, floor_time = subway_distance * 10 + subway_distance * (m * k - 1), floor_distance * 5

# Calculate the total time
total_time = subway_time + floor_time

# Print the result
print(total_time)
