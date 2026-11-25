# Read the input
hex_number = input().strip()

# Convert the hexadecimal number to an integer
decimal_number = int(hex_number, 16)

# Check if the last digit is odd
is_odd = decimal_number % 2 != 0

# Print the result
print(int(is_odd))
