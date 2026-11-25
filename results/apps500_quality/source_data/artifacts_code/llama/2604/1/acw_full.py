import math

r, d = map(int, input().split())
n = int(input())
count = 0

for _ in range(n):
	x, y, ri = map(int, input().split())
	distance = math.sqrt(x**2 + y**2)
	if distance > r - ri and distance < r - d + ri:
		count += 1

print(count)
