from sys import stdin

# Read input
a, b = map(int, stdin.read().split())

# Initialize the count of Takahashi dates
takahashi_count = 0

# Iterate over all possible month-day combinations from 1-1 to a-b
for month in range(1, a + 1):
	for day in range(1, 1 + b):
		# Check if the month and day are equal
		if month == day:
			takahashi_count += 1

# Print the result
print(takahashi_count)
