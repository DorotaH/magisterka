# Read input from standard input
a, b, c = map(int, input().split())

# Check if the arrangement of the poles is beautiful
if not b - a == c - b:
    print("NO")
else:
    print("YES")
