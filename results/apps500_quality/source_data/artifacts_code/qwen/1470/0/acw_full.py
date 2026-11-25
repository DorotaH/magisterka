import sys

# Read input
x = int(sys.stdin.read().strip())

# Calculate the minimum number of operations needed
# Since the maximum number on a die is 6, we need at least x/6 operations
# However, we can optimize this by considering the worst-case scenario
# where we need to score the minimum points first
# In this case, we need to score at least x/3 operations
# Since each operation can score a maximum of 6 points, we need at most x/3 operations
# However, we can further optimize this by considering the fact that we can score
# multiple points in a single operation if we rotate the die multiple times
# Therefore, the minimum number of operations needed is ceil(x/3)
import math
min_operations = math.ceil(x / 3)

# Print the result
print(min_operations)
