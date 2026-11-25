D, T, S = map(int, input().split())
time_required = D / S
if time_required <= T:
    print("Yes")
else:
    print("No")
