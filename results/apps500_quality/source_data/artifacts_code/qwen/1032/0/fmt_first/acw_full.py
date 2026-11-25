from math import gcd
from sys import stdin, stdout

input = stdin.read
print = stdout.write


def good_integers(n, p, a):
	# Calculate the gcd of all a_i
	gcd_a = a[0]
	for i in range(1, n):
		gcd_a = gcd(gcd_a, a[i])

	# The number of good integers x is 1 if gcd_a is not divisible by p, otherwise 0
	return (1, [gcd_a]) if gcd_a % p != 0 else (0, [])


# Read input
n, p = map(int, input().split())
a = list(map(int, input().split()))

# Find good integers
num_good, good_ints = good_integers(n, p, a)

# Print the result
print(num_good, *good_ints)
