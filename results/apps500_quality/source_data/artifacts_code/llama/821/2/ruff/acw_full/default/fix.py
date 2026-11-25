s, v1, v2, t1, t2 = map(int, input().split())

time1 = (s * (t1 + v1)) / 2
time2 = (s * (v2 + t2)) / 2

if time2 > time1:
	print("First")
elif time2 < time1:
	print("Second")
else:
	print("Friendship")
