def max_occupied_tables(n, k, s):
	# Initialize the count of free tables that can be occupied
	count = 0
	# Initialize the position of the last occupied table
	last_occupied = -k - 1

	# Iterate through the string s to count the number of valid free tables
	for i in range(n):
		if s[i] == '0' and i > last_occupied + k:
			count += 1
			last_occupied = i

	return count


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Number of test cases
t = int(data[0])
index = 1
results = []

# Process each test case
for _ in range(t):
	n = int(data[index])
	k = int(data[1 + index])
	s = data[2 + index]
	index += 3
	results.append(max_occupied_tables(n, k, s))

# Print the results
for result in results:
	print(result)
