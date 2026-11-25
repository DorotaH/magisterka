a, b, c = map(int, input().split())
print(min(min(b // a, c), c))