n = int(input())
s = input()

# Initialize a list to store the species of each animal
species=['']*(n + 1)

# Function to check if a neighbor is the same species
def same_species(i, j):
    return (s[i-1]=='o' and species[j] == species[i]) or (s[i-1]=='x' and species[j] != species[i])

# Function to check if a neighbor is different species
def diff_species(i, j):
    return (s[i-1]=='o' and species[j] != species[i]) or (s[i-1]=='x' and species[j] == species[i])

# Try to assign species to each animal
for  i in  range(1, n + 1):
    # If i is the first or last animal, assign it to be a sheep
    if i == 1 or i == n:
        species[i] = 'S'
    else:
        # If the neighbors are the same species, assign the current animal to be the same species
        if same_species(i, i-1) and same_species(i, i+1):
            species[i] = species[i-1]
        # If the neighbors are different species, assign the current animal to be the opposite species
        elif diff_species(i, i-1) and diff_species(i, i+1):
            species[i] = 'W' if species[i-1] == 'S' else 'S'

# Check if the assignment is consistent
for  i in  range(1, n + 1):
    # Check the neighbors of the current animal
    if not (same_species(i, i - 1) and same_species(i, 1+i) or diff_species(i, i - 1) and diff_species(i, 1+i)):
        print(-1)
        exit()

# Print the assignment
print(''.join(species[1:]))