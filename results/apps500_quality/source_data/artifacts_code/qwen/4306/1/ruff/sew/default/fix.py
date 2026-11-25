A, B, C, D = map(int, input().split())
start, end = max(A, C), min(B, D)
print(max(0, end - start))