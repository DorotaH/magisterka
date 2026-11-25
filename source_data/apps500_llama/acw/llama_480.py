def process_slimes(n):
	"""
	Process the slimes and return the final state of the row.
	
	Args:
		n (int): The number of slimes.
	
	Returns:
		list: The final state of the row.
	"""
	# Initialize the row with a single slime of value 1
	row = [1]
	
	# Iterate over the remaining n - 1 slimes
	for _ in range(1, n):
		# Get the last two slimes in the row
		last_two = row[-1], row[-2] if 1 < len(row) else 1
		
		# If the last two slimes have the same value, combine them
		if last_two[0] == last_two[1]:
			row[-2] += 1
		# Otherwise, add a new slime with value 1 to the right
		else:
			row.append(1)
	
	return row


def main():
	# Read the input from standard input
	n = int(input())
	
	# Process the slimes and print the result
	print(*process_slimes(n))


if __name__ == "__main__":
	main()
