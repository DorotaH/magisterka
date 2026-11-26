def determine_species(N, s):
    # Initialize the species list with None
    species = [None] * N

    # Try to assign species starting with a sheep
    species[0] = "S"
    for i in range(1, N):
        if not s[i - 1] == "o":
            if species[i - 1] == "S":
                species[i] = "W"
            else:
                species[i] = "S"
        else:
            if species[i - 1] == "S":
                species[i] = "S"
            else:
                species[i] = "W"

    # Check if the last species is consistent with the first species
    if not s[N - 1] == "o":
        if species[N - 1] == species[0]:
            return -1
        else:
            species[0] = "W" if species[0] == "S" else "S"
            if species[N - 1] == species[0]:
                return "".join(species)
            else:
                return -1
    else:
        if species[N - 1] == species[0]:
            return "".join(species)
        else:
            species[0] = "W" if species[0] == "S" else "S"
            if species[N - 1] == species[0]:
                return "".join(species)
            else:
                return -1


# Read input
N, s = int(input()), input().strip()

# Determine species and print the result
result = determine_species(N, s)
print(result)
