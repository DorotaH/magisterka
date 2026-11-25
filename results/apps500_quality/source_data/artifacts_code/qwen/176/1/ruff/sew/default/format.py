import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input
k, a = int(data[0]), int(data[1])
b = int(data[2])

# Calculate the number of k-divisible numbers in the range [a, b]
# The number of k-divisible numbers up to b is b // k
# The number of k-divisible numbers up to a-1 is (a-1) // k
# Therefore, the number of k-divisible numbers in the range [a, b] is (b // k) - ((a-1) // k)
count = (b // k) - ((a - 1) // k)

# Print the result
print(count)
