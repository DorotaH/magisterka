n, m = map(int, input().split())
prices = list()
for _ in range(0, n):
    a, b = map(int, input().split())
    prices.append((a / b, m))

prices.sort()

total = 0
for ratio, needed in prices:
    amount = min(needed, m)
    total += ratio * amount
    m -= amount

print(round(total / m, 7))
