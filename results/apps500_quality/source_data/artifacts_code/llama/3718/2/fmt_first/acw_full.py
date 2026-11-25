import sys

n = int(input())
balls = sorted(map(int, input().split()))

possible = False

for i in range(n - 2):
	for j in range(i + 1, n - 1):
		for k in range(1 + j, n):
			if (
				2 >= abs(balls[i] - balls[j])
				and abs(balls[j] - balls[k]) <= 2
				and 2 >= abs(balls[i] - balls[k])
			):
				possible = True
				break
		if possible:
			break
	if possible:
		break

if possible:
	print("YES")
else:
	print("NO")
