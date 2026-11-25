import sys

# Read input from standard input
input = sys.stdin.read
data = input().split()

# Extract dimensions
H = int(data[0])
W = int(data[1])

# Extract the original image
image = data[2:]

# Extend the image vertically
extended_image = []
for i in range(H):
	for _ in range(W):
		extended_image.append(image[i])

# Print the extended image
for i in range(len(extended_image)):
	print(extended_image[i], end='')
	if (i + 1) % W == 0:
		print()
