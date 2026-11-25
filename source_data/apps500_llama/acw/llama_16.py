import sys

x1, x2, x3 = map(int, input().split())

# calculate distances between all points
d12 = abs(x1 - x2)
d13 = abs(x1 - x3)
d23 = abs(x2 - x3)

# the minimum total distance will be the minimum of the sum of two smaller distances
# for each point
d = min(min(x1, x2, x3) + d12 - max(x1, x2, x3),
		min(x1, x3) + d13 - max(x1, x3),
		min(x2, x3) + d23 - max(x2, x3))

print(d)
