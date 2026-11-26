from collections import deque
import sys


def is_convex(n, m, grid):
    def is_convex_from_point(r, c):
        visited, queue = [[False] * m for _ in range(n)], deque([(r, c)])
        visited[r][c] = True
        up = down = left = right = None
        while queue:
            r, c = queue.popleft()
            if grid[r][c] == "B":
                if up is None:
                    up = (r - 1, c)
                if down is None:
                    down = (r + 1, c)
                if left is None:
                    left = (r, c - 1)
                if right is None:
                    right = (r, c + 1)
                if up and down and left and right:
                    return False
                if r == 0:
                    up = None
                if r == n - 1:
                    down = None
                if c == 0:
                    left = None
                if c == m - 1:
                    right = None
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr = r + dr
                nc = c + dc
                if (
                    0 <= nr < n
                    and 0 <= nc < m
                    and not visited[nr][nc]
                    and grid[nr][nc] == "B"
                ):
                    queue.append((nr, nc))
                    visited[nr][nc] = True
        return True

    for r in range(0, n):
        for c in range(m):
            if grid[r][c] == "B":
                if not is_convex_from_point(r, c):
                    return "NO"
    return "YES"


n, m = map(int, input().split())
grid = [input().strip() for _ in range(0, n)]
print(is_convex(n, m, grid))
