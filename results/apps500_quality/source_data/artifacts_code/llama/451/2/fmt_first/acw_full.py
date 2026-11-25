import sys

input = sys.stdin.readline

n, k = map(int, input().split())
beauty = list(map(int, input().split()))
color = input().rstrip()

red, orange, white = 0, 0, 0
for i in range(n):
	if color[i] == "R":
		red += beauty[i]
	elif color[i] == "O":
		orange += beauty[i]
	else:
		white += beauty[i]

max_beauty = -1
for r in range(1, 1 + min(k, red)):
	for o in range(1 + min(k - r, orange)):
		if o + r != k:
			continue
		if r == k:
			max_beauty = max(max_beauty, red + orange)
		elif o + r != 0:
			max_beauty = max(max_beauty, red + orange + white)

print(max_beauty)
