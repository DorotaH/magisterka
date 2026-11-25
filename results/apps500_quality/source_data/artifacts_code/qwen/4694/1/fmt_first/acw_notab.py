import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
a = list(map(int, data[1:]))

# Sort the array to easily find the minimum distance between the smallest and largest elements
a.sort()

# The minimum distance is between the first and last elements in the sorted array
min_distance = a[-1] - a[0]

print(min_distance)
