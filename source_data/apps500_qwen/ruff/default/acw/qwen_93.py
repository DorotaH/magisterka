import sys

# Read input
n = int(sys.stdin.read().strip())

# Calculate the minimum possible value of |sum(A) - sum(B)|
result = 0 if n % 2 == 0 else 1
# Print the result
print(result)
