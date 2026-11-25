def count_split_weights(n):
	# The number of different weights of the splits of n is given by the formula 2 * n - 1
	return 2 * n - 1


# Read input
import sys

n = int(sys.stdin.readline().strip())

# Output the result
print(count_split_weights(n))
