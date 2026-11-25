n, m = map(int, input().split())
prices = []

for _ in range(n):
    a, b = map(int, input().split())
    prices.append(a / b)

prices.sort()

total_cost = sum(prices[i] for i in range(m))
print(total_cost)
