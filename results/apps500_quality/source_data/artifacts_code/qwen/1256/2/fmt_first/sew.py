# Read the input
s = input().strip()

# Split the string into parts
parts = s.split("+")

# Convert parts to integers
numbers = list(map(int, parts))

# Sort the numbers in non-decreasing order
numbers.sort()

# Join the sorted numbers back into a string
result = "+".join(map(str, numbers))

# Print the result
print(result)