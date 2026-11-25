from collections import deque

n = int(input())
prices = []
for _ in range(n):
	a, g = map(int, input().split())
	prices.append((a, g))

price_sums = {}
for a, g in prices:
	price_sums[a] = price_sums.get(a, 0) + 1
	price_sums[g] = price_sums.get(g, 0) - 1

queue = deque([(0, 0)])  # (price_sum, current_A)
visited = {(0, 0)}
while queue:
	price_sum, current_A = queue.popleft()
	if abs(price_sum - 0) <= 500 and price_sum != 0:
		print(''.join('A' if current_A else 'G' for current_A in [price_sums[a] > 0 for a in range(1, 1001)]))
		exit()
	for a in range(1, 1001):
		new_price_sum = price_sum + price_sums.get(a, 0)
		if (new_price_sum, int(new_price_sum != 0)) not in visited:
			queue.append((new_price_sum, int(new_price_sum != 0)))
			visited.add((new_price_sum, int(new_price_sum != 0)))

print(-1)
