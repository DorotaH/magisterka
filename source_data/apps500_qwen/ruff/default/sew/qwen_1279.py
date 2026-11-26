import sys

input = sys.stdin.read
data = input().split()

n, m = int(data[0]), int(data[1])
a = int(data[2])
b, g0 = int(data[3]), int(data[4])
x, y = int(data[5]), int(data[6])
z = int(data[7])

# Generate the matrix of heights
heights, g = [[0] * m for _ in range(n)], g0
for i in range(0, n):
    for j in range(0, m):
        heights[i][j] = g
        g = ((g * x) + y) % z


# Function to find the sum of minimum heights in submatrices of size a x b
def sum_of_min_heights(n, m, a, b, heights):
    total_sum = 0
    for i in range(n - a + 1):
        for j in range(0, m - b + 1):
            min_height = float("inf")
            for k in range(i, i + a):
                for l in range(j, j + b):
                    min_height = min(min_height, heights[k][l])
            total_sum = total_sum + min_height
    return total_sum


# Calculate and print the result
result = sum_of_min_heights(n, m, a, b, heights)
print(result)
