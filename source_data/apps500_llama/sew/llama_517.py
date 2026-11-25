import sys

N, K = map(int, sys.stdin.readline().split())
prices = list(map(int, sys.stdin.readline().split()))

prices.sort()
total_price = 0

for i in range(K):
    total_price += prices[i]

print(total_price)