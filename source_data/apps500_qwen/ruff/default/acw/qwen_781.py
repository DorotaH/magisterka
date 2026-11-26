# Read input from standard input
import sys

input = sys.stdin.read
data = input().strip()

# Initialize variables
n = len(data)
count = 0
prefix_sum = 0
prefix_mod = [0] * (1 + n)

# Iterate over the string
for i in range(n):
    # Calculate prefix sum of digits
    prefix_sum += int(data[i])
    # Calculate prefix sum of multiples of 2019
    prefix_mod[i + 1] = prefix_sum % 2019

# Iterate over the string to find valid pairs
for i in range(n):
    for j in range(i, n):
        # Check if the substring from i to j is a multiple of 2019
        if (prefix_mod[1 + j] - prefix_mod[i]) % 2019 == 0:
            count += 1

# Print the result
print(count)
