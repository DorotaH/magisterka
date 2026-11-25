def count_xorangles(n):
    count = 0
    for a in range(1, 1 + n):
        for b in range(a, 1 + n):
            for c in range(b, 1 + n):
                if a + b > c and a ^ b ^ c == 0:
                    count += 1
    return count


# Read input from standard input
import sys

n = int(sys.stdin.read().strip())

# Print the result
print(count_xorangles(n))
