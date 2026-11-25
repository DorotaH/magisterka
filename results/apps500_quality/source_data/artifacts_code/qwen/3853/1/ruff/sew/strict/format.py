import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Number of different sizes of boxes
n = int(data[0])

# Dictionary to store the number of boxes for each side length
box_counts = dict()

# Process each box size and count
index = 1
for _ in range(0, n):
    k, a = int(data[index]), int(data[index + 1])
    if not k in box_counts:
        box_counts[k] = a
    else:
        box_counts[k] += a
    index += 2

# Find the maximum number of boxes for any side length
max_boxes = max(box_counts.values())

# Determine the smallest side length that can contain all the boxes
p = 0
while pow(2, p) < max_boxes:
    p = p + 1

# Output the result
print(p)
