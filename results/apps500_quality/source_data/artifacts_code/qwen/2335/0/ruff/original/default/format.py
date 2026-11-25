import sys
from heapq import heappop, heappush

# Read input from standard input
input = sys.stdin.read
data = input().split()

n = int(data[0])
points = []

for i in range(n):
    p = int(data[2 * i + 1])
    c = data[2 * i + 2]
    points.append((p, c))

# Separate points by color
red_points = [p for p, c in points if c == "R"]
green_points = [p for p, c in points if c == "G"]
blue_points = [p for p, c in points if c == "B"]


# Function to find the minimum spanning tree cost for a list of points
def min_spanning_tree_cost(points):
    if not points:
        return 0
    edges = []
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            heappush(edges, (abs(points[i] - points[j]), points[i], points[j]))
    visited = set()
    mst_cost = 0
    while edges:
        cost, u, v = heappop(edges)
        if u not in visited and v not in visited:
            visited.add(u)
            visited.add(v)
            mst_cost += cost
            if len(visited) == n:
                break
    return mst_cost


# Calculate the minimum cost for each color group
red_cost = min_spanning_tree_cost(red_points)
green_cost = min_spanning_tree_cost(green_points)
blue_cost = min_spanning_tree_cost(blue_points)

# The total cost is the sum of the minimum costs of the three groups
total_cost = red_cost + green_cost + blue_cost

# Print the result
print(total_cost)
