# Read input from standard input
grid = [input().strip() for _ in range(3)]

# Extract the diagonal elements
diagonal = [grid[i][i] for i in range(3)]

# Concatenate the diagonal elements and print the result
print("".join(diagonal))
