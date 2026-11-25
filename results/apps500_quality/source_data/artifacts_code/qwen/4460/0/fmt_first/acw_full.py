import sys

input = sys.stdin.read
data = input().split()

x = list(map(int, data))

for i in range(5):
	if x[i] == 0:
		print(i + 1)
		break
