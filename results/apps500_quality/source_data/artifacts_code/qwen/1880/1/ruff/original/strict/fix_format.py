import sys


def shuffle_and_code(number):
    # Convert the number to a string to easily access individual digits
    num_str = str(number)

    # Shuffle the digits as per the given order
    shuffled_str = num_str[0] + num_str[2] + num_str[4] + num_str[3] + num_str[1]

    # Convert the shuffled string back to an integer
    shuffled_number = int(shuffled_str)

    # Raise the shuffled number to the fifth power
    result = shuffled_number**5

    # Get the last 5 digits of the result
    activation_code = result % 100000

    return activation_code


# Read input from standard input
input_number = int(sys.stdin.read().strip())

# Calculate the activation code
activation_code = shuffle_and_code(input_number)

# Print the activation code without spaces
print(activation_code)
