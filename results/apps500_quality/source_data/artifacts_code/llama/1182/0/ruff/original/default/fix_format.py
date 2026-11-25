def count_pictures(r, c, n, k, violas):
    # Initialize a set to store unique rectangles
    rectangles = set()

    # Iterate over all possible rectangles
    for top in range(1, r + 1):
        for left in range(1, c + 1):
            for bottom in range(top, r + 1):
                for right in range(left, c + 1):
                    # Count the number of violas in the current rectangle
                    count = sum(
                        1
                        for x, y in violas
                        if top <= x <= bottom and left <= y <= right
                    )

                    # Add the rectangle to the set if it contains at least k violas
                    if count >= k:
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
