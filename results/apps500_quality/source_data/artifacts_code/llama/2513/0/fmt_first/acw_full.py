n = int(input())
s = input()

# Initialize a list to store the species of each animal
species = [""] * (1 + n)


# Function to check if a neighbor is the same species
def same_species(i, j):
	return (s[i - 1] == "o" and species[i] == species[j]) or (
		s[i - 1] == "x" and species[i] != species[j]
	)


# Function to check if a neighbor is different species
def diff_species(i, j):
	return (s[i - 1] == "o" and species[i] != species[j]) or (
		s[i - 1] == "x" and species[i] == species[j]
	)


# Try to assign species to each animal
for i in range(1, 1 + n):
	# If i is the first or last animal, assign it to be a sheep
	if i in [1, n]:
		species[i] = "S"
	elif same_species(i, i - 1) and same_species(i, i + 1):
		species[i] = species[i - 1]
	elif diff_species(i, i - 1) and diff_species(i, i + 1):
		species[i] = "W" if species[i - 1] == "S" else "S"

# Check if the assignment is consistent
for i in range(1, 1 + n):
	# Check the neighbors of the current animal
	if not (
		same_species(i, i - 1)
		and same_species(i, i + 1)
		or diff_species(i, i - 1)
		and diff_species(i, i + 1)
	):
		print(-1)
		exit()

# Print the assignment
print("".join(species[1:]))
