import math

n, m = map(int, input().split())
prices = []
for _ in range(n):
	a, b = map(int, input().split())
	prices.append((a / b, m))

prices.sort()

total = 0
for ratio, needed in prices:
	amount = min(needed, m)
	total += amount * ratio
	m -= amount

print(round(total / m, 7))
