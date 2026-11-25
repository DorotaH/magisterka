
# Read input values
H, L = map(int, input().split())

# Calculate the depth of the lake at point A
depth = (L**2 - H**2) / (2 * H)

# Print the result
print(depth)
