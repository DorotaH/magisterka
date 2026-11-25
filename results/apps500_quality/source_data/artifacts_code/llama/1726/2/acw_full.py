n, t = map(int, input().split())
a = list(map(int, input().split()))
total_time = 0
days = 0

for time in a:
	total_time += time
	days += 1
	if t <= total_time:
		print(days)
		break
	elif days == n:
		print(n)
