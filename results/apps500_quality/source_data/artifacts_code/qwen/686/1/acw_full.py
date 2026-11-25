import sys


def can_make_equal(x, y):
	return (x - y) % 2 == 0


t = int(input())
results = []

for _ in range(t):
	x, y = map(int, input().split())
	if can_make_equal(x, y):
		results.append("YES")
	else:
		results.append("NO")

for result in results:
	print(result)
