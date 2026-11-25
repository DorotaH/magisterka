k, a, b = map(int, input().split())
count = (b // k) - (a - 1) // k
print(count if k != 0 else b - a + 1)
