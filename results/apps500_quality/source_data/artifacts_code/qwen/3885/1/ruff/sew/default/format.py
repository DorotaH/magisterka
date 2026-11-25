# Read input
import sys

input = sys.stdin.read
data = input().split()

# Number of schools
n = int(data[0])

# Calculate the minimum cost to visit all schools
# The optimal strategy is to visit schools in a sequence that minimizes the cost
# Since the cost (i + j) % (n + 1) is symmetric, we can calculate the total cost by summing up the costs for a single round trip
# The total cost for a round trip from school 1 to school n and back to school 1 is:
# sum((i + (i + 1)) % (n + 1) for i in range(1, n))
# This simplifies to:
# sum((2 * i + 1) % (n + 1) for i in range(1, n))
# We can further simplify this by noting that the sum of (2 * i + 1) for i from 1 to n is n * (n + 1)
# Therefore, the total cost is:
# n * (n + 1) / 2
# However, since we are taking modulo (n + 1), we need to take the result modulo (n + 1)
# For even n, this is 0
# For odd n, this is n
# Therefore, the minimum cost is simply n if n is odd, and 0 if n is even

# Print the result
if not n % 2 == 0:
    print(n)
else:
    print(0)
