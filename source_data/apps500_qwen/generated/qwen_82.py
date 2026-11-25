# Importing the required module
from math import comb

# Function to calculate the number of ways to cover the belt-like area
def calculate_ways(n):
    # Using the comb function to calculate the binomial coefficient
    return comb(2 * n, n) // (n + 1)

# Reading the number of test cases
t = int(input())

# Processing each test case
for _ in range(t):
    n = int(input())
    # Printing the result for each test case
    print(calculate_ways(n))
