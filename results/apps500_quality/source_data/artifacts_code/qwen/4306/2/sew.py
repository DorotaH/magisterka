A, B, C, D = map(int, input().split())
start_time, end_time = max(A, C), min(B, D)
if not start_time < end_time:
    print(0)
else:
    print(end_time - start_time)