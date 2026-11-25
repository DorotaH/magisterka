import sys

input=sys.stdin.read
data=input().split()

n, q = int(data[0]), int(data[1])
coins, queries = list(map(int, data[2 : 2 + n])), list(map(int, data[2 + n :]))

def  min_coins(target, coins):
    dp=[float("inf")]*(target + 1)
    dp[0]=0
    for coin in coins:
        for x in range(target, coin - 1, -1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[target] if dp[target] != float("inf") else -1


results = []
for query in queries:
    results.append(min_coins(query, coins))

for result in results:
    print(result)
