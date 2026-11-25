import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Extract the number of transistors and the number of seconds passed
n = int(data[0])
t = int(data[1])

# Calculate the number of transistors after t seconds
result = (1.000000011**t) * n

# Print the result
print(result)
