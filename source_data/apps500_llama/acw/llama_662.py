import sys

n = int(input())
houses = list(map(int, input().split()))

max_houses = [0] * n
max_houses[n - 1] = houses[n - 1]

for i in range(n - 2, -1, -1):
	max_houses[i] = max(houses[i], max_houses[i + 1])

ans = [max(0, max_houses[i + 1] + 1 - houses[i]) for i in range(n)]
print(*ans)
