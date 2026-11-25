import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
q = int(data[1])
coins = list(map(int, data[2:2 + n]))
queries = list(map(int, data[2 + n:]))


def min_coins(target, coins):
	dp = [float('inf')] * (1 + target)
	dp[0] = 0
	for coin in coins:
		for x in range(target, coin - 1, -1):
			dp[x] = min(dp[x], 1 + dp[x - coin])
	return dp[target] if dp[target] != float('inf') else -1


results = [min_coins(query, coins) for query in queries]

for result in results:
	print(result)
