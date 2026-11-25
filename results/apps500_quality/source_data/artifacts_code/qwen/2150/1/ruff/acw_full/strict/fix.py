import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
b = list(map(int, data[1:]))

a = [0] * n
x = [0] * n

a[0] = b[0]
x[0] = 0

for i in range(1, n):
	a[i] = x[i - 1] + b[i]
	x[i] = max(x[i - 1], a[i - 1])

for i in range(n):
	a[i] = x[i - 1] + b[i]

print(" ".join(map(str, a)))
