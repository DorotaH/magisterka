a, b, c = map(int, input().split())
min_price = min(a + b, a + c, b + c)
print(min_price)
