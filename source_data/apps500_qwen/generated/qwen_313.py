import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Parse the input integers
k = int(data[0])
a = int(data[1])
b = int(data[2])

# Calculate the number of k-divisible numbers in the range [a, b]
count = (b // k) - (a - 1) // k

# Print the result
print(count)
