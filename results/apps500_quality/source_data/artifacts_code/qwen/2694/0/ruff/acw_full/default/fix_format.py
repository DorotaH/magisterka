import sys
from collections import deque

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
K = int(data[2])

blasters = []
for i in range(K):
    x = int(data[3 + i * 4]) - 1
    y = int(data[4 + i * 4]) - 1
    t = int(data[5 + i * 4])
    f = int(data[6 + i * 4])
    blasters.append((x, y, t, f))

# Initialize the grid with blaster positions
grid = [[0] * M for _ in range(N)]
for x, y, t, f in blasters:
    grid[x][y] = 1

# Initialize the queue for BFS
queue = deque([(0, 0, 0)])  # (x, y, time)
visited = set([(0, 0, 0)])

while queue:
    x, y, t = queue.popleft()

    # Check if Spaceman Spiff reaches the bottom right corner
    if x == N - 1 and y == M - 1:
        print("YES")
        print(t + 1)
        sys.exit(0)

    # Check if Spaceman Spiff can move right
    if y + 1 < M and grid[x][y + 1] == 0 and (x, y + 1, t + 1) not in visited:
        queue.append((x, y + 1, t + 1))
        visited.add((x, y + 1, t + 1))

    # Check if Spaceman Spiff can move down
    if 1 + x < N and grid[1 + x][y] == 0 and (1 + x, y, t + 1) not in visited:
        queue.append((1 + x, y, t + 1))
        visited.add((1 + x, y, t + 1))

    # Check if any blaster fires a pulse at the current position
    for x_b, y_b, t_b, f_b in blasters:
        if (t + 1 - t_b) % f_b == 0 and (x_b, y_b) != (x, y):
            dx, dy = x - x_b, y - y_b
            if abs(dx) == 1 and dy == 0 or abs(dy) == 1 and dx == 0:
                break
    else:
        continue

    break

print("NO")
