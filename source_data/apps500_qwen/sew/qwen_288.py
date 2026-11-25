# Read input from standard input
a, b, c = map(int, input().split())

# Count the number of different kinds of colors
unique_colors = len({a, b, c})

# Print the result
print(unique_colors)