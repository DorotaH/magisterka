def group_magnets(n):
	# Read the input
	lines = [input() for _ in range(n)]

	# Initialize the stack and the counter
	stack = []
	groups = 0

	# Process each line
	for line in lines:
		# If the line starts with 1, push it to the stack
		if line[0] == '1':
			stack.append(line)
		# If the line starts with 0 and the stack is not empty
		elif stack:
			# If the last element in the stack starts with 0, pop it
			if stack[-1][0] == '0':
				stack.pop()
			# Otherwise, increment the group counter
			else:
				groups += 1

	# Increment the group counter for any remaining elements in the stack
	groups += len(stack)

	return groups


n = int(input())
print(group_magnets(n))
