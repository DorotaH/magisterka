

def find_possible_values(n: int, k: int, coins: list[int]) -> list[int]:
	# Initialize a set to keep track of possible sums
	possible_sums = {0}
	
	# Iterate over each coin
	for coin in coins:
		# Create a new set to store the sums we can form by adding the current coin to existing sums
		new_sums = set()
		for s in possible_sums:
			new_sums.add(coin + s)
		# Add the new sums to the set of possible sums
		possible_sums.update(new_sums)
	
	# Filter out the sums that are greater than k
	possible_sums = {s for s in possible_sums if k >= s}
	
	return sorted(possible_sums)


# Read input
n, k = map(int, input().split())
coins = list(map(int, input().split()))

# Find and print the possible values
possible_values = find_possible_values(n, k, coins)
print(len(possible_values))
print(' '.join(map(str, possible_values)))
