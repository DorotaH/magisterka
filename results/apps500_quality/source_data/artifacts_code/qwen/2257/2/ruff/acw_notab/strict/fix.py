import numpy as np


def min_watering_area(n, x1, y1, x2, y2, flowers):
    # Convert coordinates to numpy arrays for easier manipulation
    flowers = np.array(flowers)

    # Function to calculate the squared distance from a point to a line segment
    def dist_to_segment(p, q1, q2):
        v = q2 - q1
        w = p - q1
        c1 = np.dot(w, v)
        c2 = np.dot(v, v)
        if c1 <= 0:
            return np.sum((w) ** 2)
        elif c1 >= c2:
            return np.sum((p - q2) ** 2)
        else:
            b = c1 / c2
            return np.sum((w - v * b) ** 2)

    # Function to calculate the maximum distance from a point to a set of points
    def max_distance_to_points(p, points):
        return np.max(np.sqrt(np.sum((points - p) ** 2, axis=1)))

    # Function to calculate the maximum distance from a point to a line segment
    def max_distance_to_segment(p, q1, q2):
        return np.sqrt(dist_to_segment(p, q1, q2))

    # Function to calculate the minimum r1^2 + r2^2
    def find_min_r1_r2():
        min_r1_r2 = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                q1 = flowers[i]
                q2 = flowers[j]
                r1 = max_distance_to_segment(q1, (x1, y1), (x2, y2))
                r2 = max_distance_to_segment(q2, (x1, y1), (x2, y2))
                min_r1_r2 = min(min_r1_r2, r2 ** 2 + r1 ** 2)
        return min_r1_r2

    return find_min_r1_r2()


# Read input
n, x1, y1, x2, y2 = map(int, input().split())
flowers = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
print(min_watering_area(n, x1, y1, x2, y2, flowers))
