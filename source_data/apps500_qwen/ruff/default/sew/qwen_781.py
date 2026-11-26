# Read input from standard input
import sys

input = sys.stdin.read
data = input().strip()

# Initialize variables
n = len(data)
count = 0
prefix_sum = 0
prefix_mod = [0] * (n + 1)

# Iterate over the string
for i in range(0, n):
    # Calculate prefix sum of digits
    prefix_sum += int(data[i])
    # Calculate prefix sum of multiples of 2019
    prefix_mod[i + 1] = prefix_sum % 2_019

# Iterate over the string to find valid pairs
for i in range(0, n):
    for j in range(i, n):
        # Check if the substring from i to j is a multiple of 2019
        if 0 == (prefix_mod[j + 1] - prefix_mod[i]) % 2019:
            count = count + 1

# Print the result
print(count)
