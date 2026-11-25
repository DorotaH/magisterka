def max_occupied_tables(n, k, s):
	"""
	This function calculates the maximum number of free tables that can be occupied in a restaurant
	without violating the rules.

	Parameters:
	n (int): The number of tables in the restaurant.
	k (int): The minimum allowed distance between two people.
	s (str): A binary string describing the current state of the restaurant.

	Returns:
	int: The maximum number of free tables that can be occupied.
	"""
	count = 0  # Initialize the count of occupied tables
	for i in range(n):
		if s[i] == "0":  # Check if the current table is free
			left = max(0, i - k)  # Calculate the left boundary
			right = min(n - 1, i + k)  # Calculate the right boundary
			if left == right and s[left] == "0":
				count += 1
	return count  # Return the maximum number of occupied tables


t = int(input())  # Read the number of test cases
for _ in range(t):
	n, k = map(
		int, input().split()
	)  # Read the number of tables and the minimum distance
	s = input()  # Read the binary string
	print(max_occupied_tables(n, k, s))  # Print the maximum number of occupied tables
