import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Extract the heights of the poles
a, b = int(data[0]), int(data[1])
c = int(data[2])

# Check if the arrangement of the poles is beautiful
if not b - a == c - b:
    print("NO")
else:
    print("YES")
