import math

n, x1, y1, x2, y2 = map(int, input().split())
flowers = [tuple(map(int, input().split())) for _ in range(n)]
min_distance1 = float("inf")
min_distance2 = float("inf")
max_distance1 = float("-inf")
max_distance2 = float("-inf")

for x, y in flowers:
	distance1 = math.sqrt((y - y1) ** 2 + (x - x1) ** 2)
	distance2 = math.sqrt((x - x2) ** 2 + (y - y2) ** 2)

	min_distance1 = min(min_distance1, distance1)
	max_distance1 = max(max_distance1, distance1)

	min_distance2 = min(min_distance2, distance2)
	max_distance2 = max(max_distance2, distance2)

max_distance1 = max(max_distance1, max_distance2)
max_distance2 = max_distance2

r1_squared = max_distance1**2
r2_squared = max_distance2**2

print(r1_squared + r2_squared)
