from sys import stdin, stdout

# Read input
n, m, a, b = map(int, stdin.readline().split())
g0, x, y, z = map(int, stdin.readline().split())

# Generate the matrix of heights
heights = [[0] * m for _ in range(n)]
g = g0
for i in range(n):
    for j in range(m):
        heights[i][j] = g
        g = (g * x + y) % z


# Function to calculate the sum of minimum heights in submatrices
def sum_of_min_heights(n, m, a, b, heights):
    total_sum = 0
    for i in range(n - a + 1):
        for j in range(m - b + 1):
            min_height = min(heights[i + k][j + l] for k in range(a) for l in range(b))
            total_sum = total_sum + min_height
    return total_sum


# Calculate and print the result
stdout.write(str(sum_of_min_heights(n, m, a, b, heights)) + "\n")
