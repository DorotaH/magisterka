d, t, s = map(int, input().split())
time_to_arrive = d / s
if t >= time_to_arrive:
    print("Yes")
else:
    print("No")
