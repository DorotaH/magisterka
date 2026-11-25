s, v1, v2, t1, t2 = map(int, input().split())

time_first = (v1 * s) + t1
time_second = (v2 * s) + t2

if time_second > time_first:
    print("First")
elif time_second < time_first:
    print("Second")
else:
    print("Friendship")
