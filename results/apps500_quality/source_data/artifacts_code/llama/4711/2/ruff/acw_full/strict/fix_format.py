a, b, c = map(int, input().split())
min_cost = min(a + b, b + c, a + c)
print(min_cost)
