import sys

# Read the input from standard input
hex_number = sys.stdin.read().strip()

# Convert the hexadecimal number to an integer
decimal_number = int(hex_number, 16)

# Check if the number is odd
is_odd = 0 != decimal_number % 2

# Output the result
print(int(is_odd))