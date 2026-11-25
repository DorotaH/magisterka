import sys

input = sys.stdin.read
data = input().split()

N, a = int(data[0]), list(map(int, data[1:]))

# Sort the coordinates to make it easier to find the minimum distance
a.sort()

# The minimum distance will be between the first and the last house
min_distance = a[-1] - a[0]

print(min_distance)
