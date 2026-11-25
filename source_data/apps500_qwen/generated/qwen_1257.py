def count_xorangles(n):
    count = 0
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            for c in range(b, n + 1):
                if a + b > c and a ^ b ^ c == 0:
                    count += 1
    return count

# Read input from standard input
import sys
n = int(sys.stdin.read().strip())

# Print the result
print(count_xorangles(n))
