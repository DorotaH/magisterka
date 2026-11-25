import sys


def largest_perfect_power(X):
    max_power = 0
    for b in range(1, 1 + X):
        p = 2
        while (bp := b ** p) <= X:
            max_power = max(max_power, bp)
            p += 1
    return max_power


# Read input from standard input
X = int(sys.stdin.read().strip())

# Print the largest perfect power that is at most X
print(largest_perfect_power(X))
