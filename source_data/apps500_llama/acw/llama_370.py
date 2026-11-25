s, v1, v2, t1, t2 = map(int, input().split())

time1 = (v1 * s) + 2 * t1
time2 = (v2 * s) + 2 * t2

if time2 > time1:
	print("First")
elif time2 < time1:
	print("Second")
else:
	print("Friendship")
