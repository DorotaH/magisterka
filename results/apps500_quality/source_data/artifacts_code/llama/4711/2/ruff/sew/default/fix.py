a, b, c = map(int, input().split())
min_cost = min(a + b, b + c, c + a)
print(min_cost)