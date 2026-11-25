n, m = map(int, input().split())
prices = list()

for _ in range(n):
    a, b = map(int, input().split())
    prices.append(a / b)

prices.sort()

total_cost = 0
for i in range(m):
    total_cost += prices[i]

print(total_cost)
