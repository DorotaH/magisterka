
# Read input
N, M=map(int, input().split())
ns, es = [], []
for _ in range(0, N):
    a, b, c = map(int, input().split())
    ns.append((a, b, c))
for _ in range(0, M):
    d, e, f = map(int, input().split())
    es.append((d, e, f))

# Find the minimum and maximum x and y coordinates
min_x, max_x = float('inf'), float('-inf')
min_y, max_y = float('inf'), float('-inf')

# Update the minimum and maximum x and y coordinates
for a, b, c in ns:
    min_x = min(min_x, a)
    max_x = max(max_x, b)
    min_y = min(min_y, c)
    max_y = max(max_y, c)
for d, e, f in es:
    min_x = min(min_x, e)
    max_x = max(max_x, f)
    min_y = min(min_y, f)
    max_x = max(max_x, e)

# Calculate the area of the region the cow can reach
if min_y <= 0 or max_y <= 0:
    print('INF')
else:
    # Calculate the width and height of the region
    width = max_x - min_x
    height = max_y - min_y

    # Initialize the intersection points
    isects = []

    # Check for intersections with north-south lines
    for i in range(N):
        a, b, c = ns[i]
        # Check if the line intersects with the field
        if c >= 0:
            # Check if the line intersects with the x-axis
            if a <= 0 and b >= 0:
                # Calculate the intersection point
                x = 0
                y = c
                isects.append((x, y))

    # Check for intersections with east-west lines
    for j in range(M):
        d, e, f = es[j]
        # Check if the line intersects with the field
        if f <= 0:
            # Check if the line intersects with the y-axis
            if d >= 0 and e <= 0:
                # Calculate the intersection point
                x = d
                y = 0
                isects.append((x, y))

    # Sort the intersection points
    isects.sort()

    # Calculate the area of the region
    area = width * height
    for i in range(len(isects)):
        x, y = isects[i]
        # Check if the intersection point is to the right of the cow
        if x > 0:
            # Calculate the distance from the cow to the intersection point
            dist = x
            # Subtract the distance from the area
            area -= dist * min_y
            # Update the minimum y coordinate
            min_y = min(min_y, y)

    print(area)
