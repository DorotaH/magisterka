import sys

n, k = map(int, input().split())
prices = list(map(int, input().split()))

# Sort prices in ascending order
prices.sort()

# Select the k smallest prices to minimize total cost
total_price = sum(prices[:k])

print(total_price)
