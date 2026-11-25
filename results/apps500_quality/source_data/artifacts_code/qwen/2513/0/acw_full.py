def determine_species(N, s):
	# Initialize the species list with None
	species = N * [None]

	# Try to assign species starting with a sheep
	species[0] = 'S'
	for i in range(1, N):
		if (
			s[i - 1] == 'o'
			and species[i - 1] == 'S'
			or s[i - 1] != 'o'
			and species[i - 1] != 'S'
		):
			species[i] = 'S'
		else:
			species[i] = 'W'
	if species[N - 1] == species[0]:
		return ''.join(species) if s[N - 1] == 'o' else -1
	else:
		species[0] = 'W' if species[0] == 'S' else 'S'
		if species[N - 1] == species[0]:
			return ''.join(species)
		else:
			return -1


# Read input
N = int(input())
s = input().strip()

# Determine species and print the result
result = determine_species(N, s)
print(result)
