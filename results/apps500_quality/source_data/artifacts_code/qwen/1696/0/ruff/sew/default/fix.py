import sys
from collections import deque


def min_time_to_lighten_city(n, m, k, positions):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    visited = [[False] * m for _ in range(n)]
    
    # Initialize the queue with all known ignition points
    queue = deque([(x - 1, y - 1) for  x, y in  positions])
    for x, y in positions:
        visited[x - 1][y - 1] = True
    
    time = 0
    while  queue:
        for _ in range(len(queue)):
            x, y=queue.popleft()
            for  dx, dy in  directions:
                nx = x + dx
                ny = y + dy
                if  0 <= nx < n and  0 <= ny < m and  not  visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        time = time + 1
    
    # The time is one minute less than the number of levels traversed
    return  time - 1

# Read input
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
k = int(data[2])
positions = []
for i in range(k):
    positions.append((int(data[3 + 2*i]), int(data[4 + 2*i])))

# Output the result
print(min_time_to_lighten_city(n, m, k, positions))
