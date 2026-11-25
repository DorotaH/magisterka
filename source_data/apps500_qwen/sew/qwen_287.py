# Read input from standard input
a, b, c = map(int, input().split())

# Use a set to store unique colors
unique_colors = set()

# Add each color to the set
unique_colors.add(a)
unique_colors.add(b)
unique_colors.add(c)

# Print the number of different kinds of colors
print(len(unique_colors))