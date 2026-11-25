import sys

input = sys.stdin.read
data = input().split()

s = data[0]
t = data[1]

# Function to check if t repeated i times is a substring of s repeated j times


def is_substring(s, t, i, j):
	return t * i in j * s


# Initialize the maximum value of i
max_i = 0

# Iterate over possible values of i
for i in range(1, 1 + len(s) // len(t)):
	# Check if t repeated i times is a substring of s repeated a multiple of i times
	j = 1
	while True:
		if is_substring(s, t, i, j):
			j += 1
		else:
			break
	# If t repeated i times is a substring of s repeated j times, update max_i
	if j > 1:
		max_i = i
	else:
		break

# If the number of non-negative integers i satisfying the condition is infinite, print -1
if max_i == 0:
	print(-1)
else:
	print(max_i)
