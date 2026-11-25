import sys


def  find_activation_code():
    # Read the input number from standard input
    n = int(input())

    # Split the number into a list of digits and shuffle them
    digits = list(str(n))
    digits = [digits[0], digits[2], digits[4], digits[3], digits[1]]

    # Join the shuffled digits into a single string
    shuffled_str = ''.join(digits)

    # Convert the string back to an integer and raise it to the fifth power
    result = int(shuffled_str) ** 5

    # Get the last 5 digits of the result
    activation_code = str(result)[-5:]

    # Print the activation code
    print(activation_code)

if __name__=="__main__":
    find_activation_code()
