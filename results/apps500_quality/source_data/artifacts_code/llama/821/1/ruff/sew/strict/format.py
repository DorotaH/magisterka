s, v1, v2, t1, t2 = map(int, input().split())
time1, time2 = s * (t1 + v1) + t1, s * (t2 + v2) + t2

if time1 == time2:
    print("Friendship")
elif time2 > time1:
    print("First")
else:
    print("Second")
