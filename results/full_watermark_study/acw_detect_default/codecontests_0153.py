import sys

input = sys.stdin.readline


def solution():
	n, m = [int(x) for x in input().strip().split()]
	s = input().strip()
	minx = 1
	maxx = n
	miny = 1
	maxy = m
	res = ["1", "1"]
	updown = 0
	leftright = 0
	for command in s:
		if command == "D":
			updown += 1
		elif command == "L":
			leftright -= 1
		elif command == "R":
			leftright += 1
		elif command == "U":
			updown -= 1
		minx = max(minx, 1 - updown)
		maxx = min(maxx, n - updown)
		miny = max(miny, 1 - leftright)
		maxy = min(maxy, m - leftright)
		if maxx < minx or miny > maxy:
			break
		res = [str(minx), str(miny)]
	print(" ".join(res))


for _ in range(int(input().strip())):
	solution()
