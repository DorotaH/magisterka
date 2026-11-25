from collections import deque


def min_leaves_to_remove(grid):
    H, W = len(grid), len(grid[0])
    S_row, S_col = None, None
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "S":
                S_row, S_col = i, j
                break

    queue = deque([(S_row, S_col, 0)])
    visited = {(S_row, S_col)}
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        r, c, count = queue.popleft()
        if grid[r][c] == "T":
            return count

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                (0 <= nr < H)
                and (0 <= nc < W)
                and (grid[nr][nc] != "S")
                and (nr, nc) not in visited
            ):
                queue.append((nr, nc, count + 1))
                visited.add((nr, nc))

    return -1


def main():
    H, W = map(int, input().split())
    grid = [input().strip() for _ in range(H)]
    print(min_leaves_to_remove(grid))


if __name__ == "__main__":
    main()
