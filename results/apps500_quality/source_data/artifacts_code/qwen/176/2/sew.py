k, a, b = map(int, input().split())
print(((b // k) - (a // k) + (0 == a % k)) if b >= a else 0)