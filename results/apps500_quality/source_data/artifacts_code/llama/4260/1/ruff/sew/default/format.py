# Read input from standard input
T, X = map(int, input().split())

# Calculate the number of hours that will pass in World A
hours_world_A = T / X

# Print the result with 3 decimal places
print(f"{hours_world_A:.6f}")
