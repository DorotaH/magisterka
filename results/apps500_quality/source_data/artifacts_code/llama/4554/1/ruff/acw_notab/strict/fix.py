W, a, b = map(int, input().split())
print(min(min(b - a, (W + a) - (W + b)) + W, min(a - (W + b), (W + a) - b)))
