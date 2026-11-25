# Read input from standard input
r, D, x2000 = map(int, input().split())

# Ensure r and D are within their allowed ranges
r = max(2, min(r, 5))
D = max(1, min(D, 100))

# Calculate x_{2001} to x_{2010}
for i in range(10):
    x2000 = (r * x2000) - D
    print(x2000)