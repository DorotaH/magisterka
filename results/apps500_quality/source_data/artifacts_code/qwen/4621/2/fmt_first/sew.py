import sys

# Read input
input = sys.stdin.read
data = input().split()

# Extract dimensions
H = int(data[0])
W = int(data[1])

# Extract image data
image = [list(data[2 + i * W : 2 + (i + 1) * W]) for i in range(H)]

# Extend the image vertically
extended_image = image + image

# Print the extended image
for row in extended_image:
    print("".join(row))