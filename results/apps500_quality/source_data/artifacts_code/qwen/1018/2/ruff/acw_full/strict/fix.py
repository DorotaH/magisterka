import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Number of pens
n = int(data[0])

# Current ink volumes of the pens
ink_volumes = list(map(int, data[1:]))

# Initialize variables
days = 0
pen_index = 0

# Loop through the days of the week
while days < n:
	# Use the pen for the current day (Monday to Saturday)
	if days % 7 < 6:
		if ink_volumes[pen_index] > 0:
			ink_volumes[pen_index] -= 1
			if ink_volumes[pen_index] == 0:
				print(pen_index + 1)
				break
		pen_index = (pen_index + 1) % n
		days += 1
	else:
		# Sunday is a day of rest
		days += 1
		pen_index = (pen_index + 1) % n
