import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
N = int(data[0])
a = list(map(int, data[1:]))

# Sort the list to make it easier to find the minimum distance
a.sort()

# The minimum distance to be traveled is the distance between the first and last house
min_distance = a[-1] - a[0]

# Print the result
print(min_distance)
