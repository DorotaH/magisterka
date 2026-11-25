# Read input from standard input
x, y, z = map(int, input().split())

# Swap the contents of boxes A and B
temp = x
x = y
y = temp

# Swap the contents of boxes A and C
temp = x
x = z
z = temp

# Print the contents of the boxes
print(x, y, z)