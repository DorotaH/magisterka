n, m = map(int, input().split())
c = list(map(int, input().split()))
a = list(map(int, input().split()))

wallet = a[:]
wallet.sort()
buy_count = 0
i = 0

for game_cost in c:
	if i == m:
		break
	while i < m and wallet[i] < game_cost:
		i += 1
	if i < m:
		buy_count += 1
		wallet.pop(i)
		i -= 1

print(buy_count)
