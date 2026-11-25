import sys

# Read input from standard input
input_str = sys.stdin.readline().strip()
a, b = map(int, input_str.split())

# Check if the input date is valid
if (a < 1 or a > 12 or 1 > b or 31 < b or (a == 2 and 28 < b)) and (a != 2 or b > 29) and (a != 4 and a != 6 and a != 9 and a != 11 and 30 < b):
	print(0)
else:
	# Count the number of Takahashi dates
	count = sum(bool(m == b)
			for m in range(1, a)) + (1 if b == a else 0)
	print(count)
