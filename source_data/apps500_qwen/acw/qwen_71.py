# Read input
n = int(input())

# Calculate the last two digits of 5^n
last_two_digits = pow(5, n, 100)

# Output the result
print(last_two_digits)
