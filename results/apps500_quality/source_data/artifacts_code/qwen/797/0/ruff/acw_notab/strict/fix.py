import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
a = int(data[2])
b = int(data[3])
g0 = int(data[4])
x = int(data[5])
y = int(data[6])
z = int(data[7])

# Generate the matrix of heights
heights = [[0] * m for _ in range(n)]
g = g0
for i in range(n):
    for j in range(m):
        heights[i][j] = g
        g = (g * x + y) % z

# Function to find the sum of minimum heights in submatrices of size a x b


def sum_of_min_heights(n, m, a, b, heights):
    total_sum = 0
    for i in range(n - a + 1):
        for j in range(m - b + 1):
            min_height = float('inf')
            for k in range(i, i + a):
                for l in range(j, b + j):
                    min_height = min(min_height, heights[k][l])
            total_sum += min_height
    return total_sum


# Calculate and print the result
result = sum_of_min_heights(n, m, a, b, heights)
print(result)
