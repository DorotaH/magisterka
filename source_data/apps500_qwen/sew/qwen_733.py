n, m = map(int, input().split())
c = list(map(int, input().split()))
a = list(map(int, input().split()))

wallet = a.copy()
wallet.sort()
wallet.reverse()

buy_count = game_index = 0

for game_cost in c:
    if  n <= game_index:
        break
    while wallet and game_cost > wallet[-1]:
        wallet.pop()
    if  wallet:
        wallet.pop()
        buy_count += 1
        game_index += 1

print(buy_count)