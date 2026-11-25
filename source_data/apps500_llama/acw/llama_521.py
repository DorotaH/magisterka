n = int(input())

# The minimum positive integer divisible by both 2 and N will be the LCM of 2 and N
# We can calculate LCM using the formula: LCM(a, b) = |a*b| / GCD(a, b)

import math

lcm = abs(2 * n) // math.gcd(2, n)
print(lcm)
