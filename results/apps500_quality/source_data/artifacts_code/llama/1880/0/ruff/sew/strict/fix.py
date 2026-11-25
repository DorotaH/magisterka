
# Read the input from standard input
n = input().strip()

# Convert the input string to a list of characters
n = list(n)

# Shuffle the digits
n = n[0] + n[2] + n[4] + n[3] + n[1]

# Convert the list back to a string
n = int(n)

# Raise to the power of 5 and get the last 5 digits
n = int(str(n ** 5)[-5:])

# Print the result
print(n)
