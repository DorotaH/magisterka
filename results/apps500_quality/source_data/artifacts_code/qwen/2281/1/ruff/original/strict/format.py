import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])

# Create the array a with all integers from 1 to n twice
a = [i for i in range(1, n + 1)] + [i for i in range(1, n + 1)]

# Sort the array a to minimize the sum s
a.sort()

# Print the permuted array a
print(" ".join(map(str, a)))
