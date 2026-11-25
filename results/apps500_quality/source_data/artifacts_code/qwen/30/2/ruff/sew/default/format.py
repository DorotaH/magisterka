import sys
from math import gcd

# Read input
input = sys.stdin.read
data = input().split()

# Parse input
m, x = int(data[0]), int(data[1])

# Calculate the minimum number of traps needed
# Since gcd(x, m) = 1, the sequence x, 2x, 3x, ..., mx (mod m) will cover all rooms
# The minimum number of traps needed is the number of distinct positions in the first cycle
# This is equivalent to the order of x modulo m, which is the smallest positive integer k such that kx ≡ 1 (mod m)
# Since gcd(x, m) = 1, the order of x modulo m is a divisor of m-1
# The minimum number of traps needed is m

# Output the result
print(m)
