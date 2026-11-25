A, B, C, D = map(int, input().split())
start_time = max(A, C)
end_time = min(B, D)
if start_time < end_time:
    print(end_time - start_time)
else:
    print(0)
