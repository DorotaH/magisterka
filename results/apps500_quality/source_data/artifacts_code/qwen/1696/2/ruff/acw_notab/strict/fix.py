import sys
from collections import deque


def min_time_to_lighten_up_city(n, m, k, centers):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    max_steps = max(n, m)  # The maximum possible distance in a grid of size n x m

    def can_reach_all_blocks(start_x, start_y):
        visited = [[False] * m for _ in range(n)]
        queue = deque([(start_x, start_y)])
        visited[start_x][start_y] = True

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

        return all(visited[x][y] for x, y in centers)

    # Try placing the unknown center at each possible position and check if it can reach all blocks
    for i in range(n):
        for j in range(m):
            if all((i, j) != (x, y) for x, y in centers) and can_reach_all_blocks(i, j):
                return max_steps

    return -1  # This should never happen as per problem constraints


# Read input
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
k = int(data[2])
centers = [(int(data[3 + i * 2]), int(data[4 + i * 2])) for i in range(k)]

# Calculate and print the result
print(min_time_to_lighten_up_city(n, m, k, centers))
