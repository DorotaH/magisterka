import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])

if n == 1:
	print(1)
else:
	slimes = [1]
	for _ in range(1, n):
		slimes.append(1)
		while 2 <= len(slimes) and slimes[-1] == slimes[-2]:
			slimes.pop()
			slimes[-1] += 1
	print(*slimes)
