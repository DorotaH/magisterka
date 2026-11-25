# Read input from standard input
number = input()

# Split the input into a list of digits
digits = list(number)

# Shuffle the digits
digits = [digits[0]] + [digits[2]] + [digits[4]] + [digits[3]] + [digits[1]]

# Convert the list back to a string
shuffled_number = "".join(digits)

# Convert the string to an integer
shuffled_number = int(shuffled_number)

# Raise the number to the fifth power
result = shuffled_number**5

# Get the last 5 digits of the result
activation_code = str(result)[-5:]

# Print the activation code
print(activation_code)