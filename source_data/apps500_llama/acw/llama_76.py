import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))

for i in range(n - 1):
	while 2 + h[i] <= h[i + 1]:
		h[i] += 1
		h[i + 1] -= 1

print(*h)
