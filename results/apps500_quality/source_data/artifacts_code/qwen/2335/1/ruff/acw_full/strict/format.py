import sys
from typing import List


def minimum_cost(n: int, points: List[List[int]]) -> int:
    # Separate points by color
    red_points = [p for p, c in points if c == "R"]
    blue_points = [p for p, c in points if c == "B"]
    green_points = [p for p, c in points if c == "G"]

    # Calculate the minimum cost to connect red points and green points
    red_cost = (
        min(red_points[i + 1] - red_points[i] for i in range(len(red_points) - 1))
        if len(red_points) > 1
        else 0
    )
    green_cost = (
        min(green_points[i + 1] - green_points[i] for i in range(len(green_points) - 1))
        if len(green_points) > 1
        else 0
    )

    # Calculate the minimum cost to connect blue points and green points
    blue_cost = (
        min(blue_points[i + 1] - blue_points[i] for i in range(len(blue_points) - 1))
        if len(blue_points) > 1
        else 0
    )

    # The total minimum cost is the sum of the above costs
    return red_cost + blue_cost + green_cost


# Read input
input = sys.stdin.read
data = input().split()

n = int(data[0])
points = [[int(data[i]), data[i + 1]] for i in range(1, 2 * n, 2)]
# Calculate and print the minimum cost
print(minimum_cost(n, points))
