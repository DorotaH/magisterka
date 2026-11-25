import sys

# Read input from standard input
N = int(sys.stdin.read().strip())

# Calculate the sum of the digits of N
digit_sum = sum(int(digit) for digit in str(N))

# Check if the sum of the digits is a multiple of 9
if digit_sum % 9 == 0:
    print("Yes")
else:
    print("No")
