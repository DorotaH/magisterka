# Read the number of books from standard input
n = int(input())

# Calculate the number of digits needed to number all the books
# This is equivalent to the sum of the digits in the numbers from 1 to n
# We can use the formula for the sum of the digits of the numbers from 1 to n
# This formula is (n*(n+1))/2 * (1 + floor(log10(n)))
import math
digits = (n * (1 + n)) // 2 * (1 + math.floor(math.log10(n)))

# Print the result to standard output
print(digits)
