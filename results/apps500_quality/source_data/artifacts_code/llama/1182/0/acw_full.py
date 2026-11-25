import sys


def count_pictures(r, c, n, k, violas):
	# Initialize a set to store unique rectangles
	rectangles = set()

	# Iterate over all possible rectangles
	for top in range(1, 1 + r):
		for left in range(1, 1 + c):
			for bottom in range(top, 1 + r):
				for right in range(left, 1 + c):
					# Count the number of violas in the current rectangle
					count = sum(bool(top <= x <= bottom and left <= y <= right)
							for x, y in violas)

					# Add the rectangle to the set if it contains at least k violas
					if k <= count:
						# Store the rectangle as a tuple of its coordinates
						rectangle = (top, left, bottom, right)
						rectangles.add(rectangle)

	return len(rectangles)


r, c, n, k = map(int, input().split())
violins = set()
violas = set()
for _ in range(n):
	x, y = map(int, input().split())
	if y == 1:
		violas.add((x, 1))
	else:
		violins.add((x, y))

print(count_pictures(r, c, n, k, violas | violins))
