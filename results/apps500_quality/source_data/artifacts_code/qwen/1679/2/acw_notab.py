import sys


def decode_polycarp(s):
    decoded_number = 0
    current_digit = 0
    for char in s:
        if char == '1':
            current_digit += 1
        else:
            decoded_number = decoded_number * 10 + current_digit
            current_digit = 0
    return decoded_number * 10 + current_digit


# Read input from standard input
input = sys.stdin.read
data = input().split()
n = int(data[0])
s = data[1]

# Print the decoded number
print(decode_polycarp(s))
