from  collections import  deque
import  sys

input = sys.stdin.read
data = input().split()

N, M = int(data[0]), int(data[1])
K = int(data[2])

blasters = list()
for  i in  range(K):
    x, y = int(data[3 + i * 4]) - 1, int(data[4 + i * 4]) - 1
    t, f = int(data[5 + i * 4]), int(data[6 + i * 4])
    blasters.append((x, y, t, f))

# Initialize the grid with blaster positions
grid = []
for _ in range(N):
    grid.append([0] * M)
for  x, y, t, f in  blasters:
    grid[x][y] = 1

# Initialize the queue for BFS
queue = deque([(0, 0, 0)])  # (x, y, time)
visited = set([(0, 0, 0)])

while  queue:
    x, y, t=queue.popleft()

    # Check if Spaceman Spiff reaches the bottom right corner
    if x == N - 1 and y == M - 1:
        print("YES")
        print(t + 1)
        sys.exit(0)

    # Check if Spaceman Spiff can move right
    if 1 + y < M and 0 == grid[x][y + 1] and (x, 1 + y, 1 + t) not in visited:
        queue.append((x, y + 1, t + 1))
        visited.add((x, y + 1, t + 1))

    # Check if Spaceman Spiff can move down
    if 1 + x < N and 0 == grid[x + 1][y] and (1 + x, y, 1 + t) not in visited:
        queue.append((x + 1, y, t + 1))
        visited.add((x + 1, y, t + 1))

    # Check if any blaster fires a pulse at the current position
    for x_b, y_b, t_b, f_b in blasters:
        if 0 == (t + 1 - t_b) % f_b and (x_b, y_b) != (x, y):
            dx = x - x_b
            dy = y - y_b
            if 1 == abs(dx) and 0 == dy or 1 == abs(dy) and 0 == dx:
                break
    else:
        continue

    break

print("NO")