n = int(input())
a = list(map(int, input().split()))

# Initialize variables
days_in_week = 7
current_day = 0
current_pen = 0

# Loop through the days of the week
for _ in range(days_in_week):
	# Update the current pen and its ink
	current_pen = (1 + current_pen) % n
	if current_day == 0:
		a[current_pen] -= 1
		if a[current_pen] == 0:
			print(1 + current_pen)
			break
	current_day = (current_day + 1) % days_in_week
