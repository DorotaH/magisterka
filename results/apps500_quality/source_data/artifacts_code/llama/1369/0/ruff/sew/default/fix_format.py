import math


def calculate_min_radius(points):
    """
    Calculate the minimum radius of a circle that encloses all points.

    Args:
    points (list): List of points (x, y) in a two-dimensional plane.

    Returns:
    float: The minimum radius of a circle that encloses all points.
    """
    # Find the center of the circle
    n = len(points)
    centroid_x = sum(x for x, y in points) / n
    centroid_y = sum(y for x, y in points) / n

    # Find the minimum distance from the center to any point
    min_distance = float("inf")
    for x, y in points:
        distance = math.sqrt(pow((x - centroid_x), 2) + pow((y - centroid_y), 2))
        min_distance = min(min_distance, distance)

    # The minimum radius is the distance from the center to the farthest point
    return min_distance


def main():
    # Read the number of points
    n = int(input())

    # Read the points
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    # Calculate and print the minimum radius
    radius = calculate_min_radius(points)
    print(f"{radius:.6f}")  # Print with 6 decimal places


if __name__ == "__main__":
    main()
