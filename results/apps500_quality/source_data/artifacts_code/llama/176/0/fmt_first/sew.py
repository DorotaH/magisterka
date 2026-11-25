k, a, b = map(int, input().split())
count = (b // k) - (-(-a // k) if a < 0 else 0) + 1
print(count)