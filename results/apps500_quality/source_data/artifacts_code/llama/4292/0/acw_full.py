import sys

N, K = map(int, sys.stdin.readline().split())
prices = list(map(int, sys.stdin.readline().split()))

prices.sort()
total_price = sum(prices[i] for i in range(K))
print(total_price)
