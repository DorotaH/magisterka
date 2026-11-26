import sys

# Read the number of rows and columns
H, W = map(int, input().split())

# Read the image
image = [list(input().rstrip("\n")) for _ in range(H)]

# Extend the image vertically
for i in range(H // 2):
    image.insert(0, ["." if pixel == "." else "*" for pixel in image[i + H // 2]])

# Print the extended image
for row in image:
    print("".join(row))
