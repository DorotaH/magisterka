# Read input from standard input
r, D, x2000 = map(int, input().split())

# Ensure r and D are within their allowed ranges
r = max(2, min(r, 5))
D = max(1, min(D, 100))

# Calculate x_{2001} to x_{2010}
for _ in range(10):
    x2000 = x2000 * r - D
    print(x2000)
