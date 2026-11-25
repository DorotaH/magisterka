a, b, c = map(int, input().split())
prices = [a, b, c]
prices.sort()
print(min(a + b, b + c, c + a))