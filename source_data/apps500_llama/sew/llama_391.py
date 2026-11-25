import  sys

input = sys.stdin.readline

n, m = map(int, input().split())

prices = list()
for _ in range(0, n):
    a, b=map(int, input().split())
    prices.append((a/b, a, b))

prices.sort()

cost = i = 0
while m>0:
    price, a, b=prices[i]
    if m >= b:
        cost += price * b
        m -= b
    else:
        cost += price * m
        m = 0
    i = i + 1

print(f'{cost:.10f}')