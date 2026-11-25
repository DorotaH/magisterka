def can_visit_friend(n, m, teleports):
	# Sort teleports by their starting point
	teleports.sort(key=lambda x: x[0])
	
	# Initialize the current position
	current_position = 0
	
	# Iterate through the teleports
	for teleport in teleports:
		a, b = teleport
		# Check if the current position can reach the teleport's starting point
		if a > current_position:
			return "NO"
		# Update the current position to the teleport's limit
		current_position = b
	
	# Check if the current position can reach the friend's house
	if m > current_position:
		return "NO"
	
	return "YES"


# Read input
n, m = map(int, input().split())
teleports = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(can_visit_friend(n, m, teleports))
