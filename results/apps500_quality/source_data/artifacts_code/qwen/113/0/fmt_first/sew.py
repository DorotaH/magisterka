import sys

# Read input from standard input
input_data = sys.stdin.read().strip()
n, k = map(int, input_data.split())

# Calculate k-rounding of n
if not k == 0:
    power_of_ten = 10**k
    result = ((n + power_of_ten - 1) // power_of_ten) * power_of_ten
else:
    result = n

# Print the result
print(result)