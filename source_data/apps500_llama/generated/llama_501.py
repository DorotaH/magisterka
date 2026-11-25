d, t, s = map(int, input().split())
time_to_arrive = d / s
if time_to_arrive <= t:
    print("Yes")
else:
    print("No")
