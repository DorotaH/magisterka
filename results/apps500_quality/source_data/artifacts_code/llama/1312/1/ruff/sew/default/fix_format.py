# Read input from standard input
input_str = input()
n, m = map(int, input_str.split())

# Calculate the base number of candies for each friend
base = n // m
# Calculate the remainder (number of candies that can't be evenly distributed)
remainder = n % m

# Initialize the output list with the base number of candies
output = [base] * m

# Distribute the remainder among the friends
for i in range(remainder):
    output[i] += 1

# Print the output list, separated by spaces
print(" ".join(map(str, output)))
