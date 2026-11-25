n, m = map(int, input().split())
c = list(map(int, input().split()))
a = list(map(int, input().split()))

wallet = a.copy()
wallet.sort()
wallet.reverse()

buy_count = 0
game_index = 0

for game_cost in c:
	if game_index >= n:
		break
	while wallet and wallet[-1] < game_cost:
		wallet.pop()
	if wallet:
		wallet.pop()
		buy_count += 1
		game_index += 1

print(buy_count)
