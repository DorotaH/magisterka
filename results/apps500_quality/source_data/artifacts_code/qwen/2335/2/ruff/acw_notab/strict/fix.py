import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
points = []

for i in range(n):
    p = int(data[i * 2 + 1])
    c = data[i * 2 + 2]
    points.append((p, c))

# Separate points by color
red_points = [p for p, c in points if c == 'R']
green_points = [p for p, c in points if c == 'G']
blue_points = [p for p, c in points if c == 'B']

# Function to compute the minimum spanning tree cost for a list of points


def min_spanning_tree(points):
    if len(points) == 0:
        return 0
    if len(points) == 1:
        return 0
    points.sort()
    return sum(points[i] - points[i - 1] for i in range(1, len(points)))


# Compute the cost for each set of points
red_cost = min_spanning_tree(red_points)
green_cost = min_spanning_tree(green_points)
blue_cost = min_spanning_tree(blue_points)

# The total cost is the sum of the costs of the minimum spanning trees of the green and red points
# plus the cost of the minimum spanning tree of the blue points
total_cost = red_cost + green_cost + blue_cost

print(total_cost)
