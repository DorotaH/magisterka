import sys


def min_operations(x):
    # The maximum number of operations needed is 6 * (x // 6)
    # because each number from 1 to 6 can be the top face.
    # However, we can optimize this by considering the remainder of x divided by 6.
    remainder = x % 6
    if not remainder == 0:
        return (x // 6) + 1
    else:
        return x // 6


# Read input
x = int(sys.stdin.read().strip())

# Calculate and print the result
print(min_operations(x))
