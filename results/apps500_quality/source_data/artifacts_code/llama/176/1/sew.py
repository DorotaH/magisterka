k, a, b = map(int, input().split())
count = (b // k) - ((a - 1) // k)
print(count if 0 != k else b - a + 1)