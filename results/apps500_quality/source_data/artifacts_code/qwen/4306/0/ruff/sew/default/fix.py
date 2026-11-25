A, B, C, D = map(int, input().split())
start, end = max(A, C), min(B, D)
if not start < end:
    print(0)
else:
    print(end - start)