A, B, C = map(int, input().split())
remaining = C - (A - B)
print(max(0, remaining))