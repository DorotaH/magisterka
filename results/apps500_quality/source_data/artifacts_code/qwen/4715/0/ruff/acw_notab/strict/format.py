# Read input from standard input
a, b, c = map(int, input().split())

# Create a set to store unique colors
unique_colors = {a, b, c}

# Print the number of unique colors
print(len(unique_colors))
