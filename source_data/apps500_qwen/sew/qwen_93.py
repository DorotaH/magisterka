import sys

# Read input
n = int(sys.stdin.read().strip())

# Calculate the minimum possible value of |sum(A) - sum(B)|
if n % 2 == 0:
    result = 0
else:
    result = 1

# Print the result
print(result)