import sys

input = sys.stdin.read().strip()

# Extract the first character and the rest of the string
first_char = input[0]
rest_of_string = input[1:]

# Check if the first character is 'A'
if first_char != 'A':
    print("WA")
    exit()

# Find the position of the first 'C' in the rest of the string
first_c_position = rest_of_string.find('C')

# Check if there is exactly one 'C' and it is in the correct position
if first_c_position == -1 or first_c_position != 2:
    print("WA")
    exit()

# Check if all remaining characters are lowercase
remaining_chars = rest_of_string[first_c_position + 1:]
if not remaining_chars.islower():
    print("WA")
    exit()

# If all conditions are satisfied, print "AC"
print("AC")
