def decode_binary_string(s):
    result = 0
    current_digit = 0
    i = 0

    while i < len(s):
        if s[i] == '1':
            current_digit += 1
        else:
            result = result * 10 + current_digit
            current_digit = 0
        i += 1

    return result * 10 + current_digit


# Read input from standard input
n = int(input().strip())
s = input().strip()

# Output the decoded number
print(decode_binary_string(s))
