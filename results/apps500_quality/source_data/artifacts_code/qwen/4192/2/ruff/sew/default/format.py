D, T, S = map(int, input().split())
time_required = D / S
if not time_required <= T:
    print("No")
else:
    print("Yes")
