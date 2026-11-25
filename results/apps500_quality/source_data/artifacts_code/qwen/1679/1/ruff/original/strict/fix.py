def decode_binary_string(s):
    decoded_number = 0
    current_digit = 0
    i = 0

    while i < len(s):
        if s[i] == '1':
            current_digit += 1
        else:
            decoded_number += current_digit
            current_digit = 0
        i += 1

    # Add the last digit
    decoded_number += current_digit

    return decoded_number

# Read input from standard input
n = int(input().strip())
s = input().strip()

# Print the decoded number
print(decode_binary_string(s))
