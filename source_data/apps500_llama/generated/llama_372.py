s, v1, v2, t1, t2 = map(int, input().split())

time1 = (s * (v1 + t1)) / 2
time2 = (s * (v2 + t2)) / 2

if time1 < time2:
    print("First")
elif time2 < time1:
    print("Second")
else:
    print("Friendship")
