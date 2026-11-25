import sys

input = sys.stdin.readline

n = int(input())

a = list(range(1, 2 * n + 1))

for i in range(n // 2):
	a[i * 2], a[n + i * 2] = a[n + i * 2], a[i * 2]

print(*a)
