# Read input
import sys

input = sys.stdin.read
data = input().split()

# Parse the number of rectangles
n = int(data[0])

# Initialize a 100x100 table with all values set to 0
table = [[0] * 100 for _ in range(100)]

# Process each rectangle
index = 1
for _ in range(n):
    x1, y1, x2, y2 = map(int, data[index:4 + index])
    index += 4
    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            table[i][j] += 1

# Calculate the sum of all values in the table
result = sum(sum(row) for row in table)

# Print the result
print(result)
