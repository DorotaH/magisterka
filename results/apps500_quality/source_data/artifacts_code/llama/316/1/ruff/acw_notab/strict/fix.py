# Read the input
n = int(input())

# Calculate the number of cells in the rhombus
# The formula is the sum of the first n natural numbers plus the number of cells in a (n-1)th rhombus
# The number of cells in a kth rhombus is k^2
result = (n - 1)**2 + n**2 - (n - 1)

# Print the result
print(result)
