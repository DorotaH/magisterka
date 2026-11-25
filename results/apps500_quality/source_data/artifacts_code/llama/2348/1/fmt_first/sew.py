# Read the hexadecimal number from standard input
hex_num = input().lstrip("A")

# Convert the hexadecimal number to an integer and check if it's divisible by 17
print(0 == int(hex_num, 16) % 17)