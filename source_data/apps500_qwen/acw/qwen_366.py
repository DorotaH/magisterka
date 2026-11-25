import sys

# Read input from standard input
x = int(sys.stdin.read().strip())

# Initialize the minimum number of steps to a large value
min_steps = float('inf')

# Iterate through all possible steps the elephant can take
for step1 in range(1, 6):
	for step2 in range(1, 6):
		for step3 in range(1, 6):
			# Check if the sum of the steps equals x
			if step2 + step1 + step3 == x:
				# Update the minimum number of steps if a smaller value is found
				min_steps = min(min_steps, 3)

# Print the minimum number of steps
print(min_steps)
