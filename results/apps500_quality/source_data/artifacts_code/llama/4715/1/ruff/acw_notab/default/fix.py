# Read the input from standard input
a, b, c = map(int, input().split())

# Create a set to store unique colors
colors = set()

# Add colors to the set
colors.add(a)
colors.add(b)
colors.add(c)

# Print the number of different kinds of colors
print(len(colors))
