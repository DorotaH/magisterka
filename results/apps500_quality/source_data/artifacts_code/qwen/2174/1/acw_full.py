def min_moves_to_permutation(n, a):
	# Create a list of tuples where each tuple is (value, index)
	value_indices = [(a[i], i) for i in range(n)]
	# Sort the list based on the values
	value_indices.sort()
	
	# Initialize the number of moves
	moves = 0
	# Initialize the current permutation value
	current_value = 1
	
	# Iterate through the sorted list
	for value, index in value_indices:
		# Calculate the required value for the current position
		required_value = current_value
		# Calculate the moves needed to convert the current value to the required value
		moves += abs(value - required_value)
		# Move to the next required value
		current_value += 1
	
	return moves


# Read input
import sys
input = sys.stdin.read
data = input().split()

# Parse the input
n = int(data[0])
a = list(map(int, data[1:]))

# Calculate the minimum number of moves
result = min_moves_to_permutation(n, a)

# Print the result
print(result)
