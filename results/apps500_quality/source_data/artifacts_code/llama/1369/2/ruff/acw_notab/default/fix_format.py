import math


def dist(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def min_circle(points):
    """Find the minimum radius of a circle that contains all points."""
    n = len(points)
    if n == 1:
        # If only one point, the circle is just that point
        return 0

    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]

    # Calculate the center of the circle using the mean of the points
    center_x = sum(x_coords) / n
    center_y = sum(y_coords) / n

    # Initialize minimum radius to the maximum possible value
    min_radius = float("inf")

    for point in points:
        # Calculate the distance between the current point and the center
        d = dist(point[0], point[1], center_x, center_y)
        # Update the minimum radius if necessary
        min_radius = min(min_radius, d)

    return min_radius


# Read input from standard input
n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

# Calculate and print the minimum radius
print(f"{min_circle(points):.10f}")
