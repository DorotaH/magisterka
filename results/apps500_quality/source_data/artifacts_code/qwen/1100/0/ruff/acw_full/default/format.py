# Read input
n = int(input().strip())

# Calculate the minimum number of jumps Ada has to make
# For a regular convex polygon with n vertices, the minimum number of jumps is n*(n-3)//2
min_jumps = (n - 3) * n // 2

# Print the result
print(min_jumps)
