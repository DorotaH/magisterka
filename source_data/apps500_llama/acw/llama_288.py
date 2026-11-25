# Read input from standard input
a, b, c = map(int, input().split())

# Convert input to a set to remove duplicates and count the number of elements
unique_colors = len(set([a, b, c]))

# Print the result
print(unique_colors)
