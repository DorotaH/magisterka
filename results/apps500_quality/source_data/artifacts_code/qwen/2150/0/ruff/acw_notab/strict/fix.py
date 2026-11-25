def restore_array(b):
    n = len(b)
    a = [0] * n
    x = 0
    for i in range(1, n):
        x = max(x, a[i - 1])
        a[i] = x + b[i]
    return a


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Number of elements
n = int(data[0])

# Array b
b = list(map(int, data[1:]))

# Restore array a
a = restore_array(b)

# Print result
print(' '.join(map(str, a)))
