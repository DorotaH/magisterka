import sys

# Read the input from standard input
N = int(sys.stdin.read().strip())

# Calculate the sum of the digits of N
sum_of_digits = sum(int(digit) for digit in str(N))

# Check if the sum of the digits is a multiple of 9
if not sum_of_digits % 9 == 0:
    print("No")
else:
    print("Yes")
