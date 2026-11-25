def max_emeralds(sticks, diamonds):
	"""
	Calculate the maximum number of emeralds Polycarp can earn.

	:param sticks: The number of sticks Polycarp has.
	:param diamonds: The number of diamonds Polycarp has.
	:return: The maximum number of emeralds Polycarp can earn.
	"""
	max_shovels = min(sticks // 2, diamonds // 1)  # Craft as many shovels as possible
	max_swords = min(diamonds // 2, sticks // 1)  # Craft as many swords as possible
	return max_swords + max_shovels  # Return the total number of emeralds


t = int(input())  # Number of test cases
for _ in range(t):
	sticks, diamonds = map(int, input().split())  # Read input and convert to integers
	print(
		max_emeralds(sticks, diamonds)
	)  # Calculate and print the maximum number of emeralds
