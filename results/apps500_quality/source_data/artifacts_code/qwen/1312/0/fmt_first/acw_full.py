import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])

# Calculate the base number of candies each friend gets
base = n // m
# Calculate the remainder
remainder = n % m

# Create the list with the base number of candies
result = [base] * m

# Distribute the remainder to the first 'remainder' friends
for i in range(remainder):
	result[i] += 1

# Print the result
print(" ".join(map(str, result)))
