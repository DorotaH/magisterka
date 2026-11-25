import sys

# Read input from standard input
x = int(sys.stdin.read().strip())

# The minimum number of operations needed to score at least x points
# is the smallest integer n such that n * 6 >= x
# This is because the maximum points you can score in one operation is 6
# Therefore, the minimum number of operations is ceil(x / 6)
min_operations = (x + 5) // 6

# Print the answer to standard output
print(min_operations)
