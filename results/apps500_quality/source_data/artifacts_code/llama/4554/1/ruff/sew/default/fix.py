W, a, b = map(int, input().split())
print(min(min(b - a, (a + W) - (b + W)) + W, min(a - (b + W), (a + W) - b)))