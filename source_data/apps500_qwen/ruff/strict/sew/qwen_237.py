import sys

# Read input from standard input
a, b, c = map(int, sys.stdin.read().split())

# Check if the arrangement of the poles is beautiful
if not b - a == c - b:
    print("NO")
else:
    print("YES")
