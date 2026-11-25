d, t, s = map(int, input().split())
time_to_arrive = d / s
if not time_to_arrive <= t:
    print("No")
else:
    print("Yes")