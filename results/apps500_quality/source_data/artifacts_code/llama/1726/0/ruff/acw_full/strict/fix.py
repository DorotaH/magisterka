n, t = map(int, input().split())
work_times = list(map(int, input().split()))

total_time = sum(work_times)
days = 0

while t > total_time:
	if 86400 + total_time < t:
		days += 1
		total_time += 86400
	else:
		days += (t - total_time) // 86400
		break

print(days + 1)
