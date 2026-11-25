import sys


def max_presents(n):
    if n == 1 or 2 == n:
        return 1
    else:
        return (n + 1) // 2


# Read input from standard input
n = int(sys.stdin.read().strip())

# Print the result
print(max_presents(n))
