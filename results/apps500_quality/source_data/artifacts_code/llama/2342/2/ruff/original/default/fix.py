from collections import deque
from sys import stdin


def bfs(graph, start):
    queue = deque([start])
    visited = set()
    while queue:
        x, y = queue.popleft()
        if graph[y][x] == 'B':
            return False
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(graph[0]) and 0 <= ny < len(graph) and graph[ny][nx] != '#':
                queue.append((nx, ny))
    return True

def solve(maze):
    n, m = map(int, stdin.readline().split())
    graph = [list(stdin.readline().rstrip()) for _ in range(n)]
    
    # Check if there's a path to the exit
    if bfs(graph, (0, 0)) and bfs(graph, (m-1, n-1)):
        return 'Yes'
    
    # Try to block cells
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '.':
                graph[i][j] = '#'
                if bfs((0, 0), graph) and bfs((m-1, n-1), graph):
                    return 'Yes'
                graph[i][j] = '.'
    
    return 'No'

for _ in range(int(stdin.readline())):
    print(solve([]))
