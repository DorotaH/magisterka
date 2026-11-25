import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Extract N and the list of a_i values
N = int(data[0])
a = list(map(int, data[1:]))

# Initialize the maximum value of f
max_f = 0

# Iterate over possible values of m
for m in range(1, 10**6):
	# Calculate the value of f for the current m
	current_f = sum(m % ai for ai in a)
	# Update the maximum value of f if the current value is greater
	if current_f > max_f:
		max_f = current_f

# Print the maximum value of f
print(max_f)
