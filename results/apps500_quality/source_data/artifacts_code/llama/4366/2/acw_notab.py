# Read the input from standard input
A, B = map(int, input().split())

# Calculate the starting time
starting_time = (B + A) % 24

# Print the result
print(starting_time)
