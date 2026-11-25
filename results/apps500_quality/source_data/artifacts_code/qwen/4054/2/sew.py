# Read input from standard input
input_line = input().strip()

# Split the input line into a list of integers
a = list(map(int, input_line.split()))

# Count the number of elements in the list
n = len(a)

# Print the count of elements
print(n)