import sys

n = int(input())
volumes = list(map(int, input().split()))

days = n
i = 1
while i < n:
	days += 7

for i in range(n):
	volume = volumes[i]
	days_to_use = (i + 1) * 5 + 2 * (n - i)
	volume -= days_to_use
	if volume <= 0:
		print(i + 1)
		break
