import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Number of pairs
n = int(data[0])

# List to store the number of operations for each pair
operations = []

# Index to track the current position in the data list
index = 1

# Process each pair
for _ in range(n):
	a = int(data[index])
	b = int(data[1 + index])
	count = 0

	# Perform the operation until one of the numbers becomes zero
	while a > 0 and 0 < b:
		if a > b:
			a -= b
		else:
			b -= a
		count += 1

	# Append the number of operations for this pair to the list
	operations.append(count)

	# Move the index forward by 2 to get the next pair
	index += 2

# Print the results
print(*operations)
