from  collections import  deque


def get_adjacent_cells(H, W, i, j):
    """Get adjacent cells in the same row or column as the given cell."""
    adjacent_cells=list()
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni = i + di
        nj = j + dj
        if 0 <= ni < H and 0 <= nj < W:
            adjacent_cells.append((ni, nj))
    return  adjacent_cells


def dfs(H, W, grid, i, j, T_i, T_j, removed):
    """Depth-first search to find a path from S to T."""
    queue=deque([(i, j, False)])  # (i, j, visited)
    while queue:
        i, j, visited = queue.popleft()
        if (i, j) == (T_i, T_j):
            return  True
        for ni, nj in get_adjacent_cells(H, W, i, j):
            if (ni, nj) != (T_i, T_j) and not grid[ni][nj] == "o":
                queue.append((ni, nj, visited))
            elif not  visited and  grid[ni][nj] == "o":
                queue.append((ni, nj, True))
    return  False


def min_leaves_to_remove(H, W, grid):
    """Find the minimum number of leaves to remove to prevent the frog from reaching T."""
    S_i, S_j=None, None
    for i in range(0, H):
        for j in range(0, W):
            if grid[i][j] == "S":
                S_i = i
                S_j = j
                break
    T_i, T_j=None, None
    for i in range(0, H):
        for j in range(0, W):
            if grid[i][j] == "T":
                T_i = i
                T_j = j
                break

    # DFS to find a path from S to T
    if not dfs(H, W, grid, S_i, S_j, T_i, T_j, set()):
        # If a path exists, remove as many leaves as possible without creating a path
        return -1
    else:
        min_removed = 0
        for i in range(H):
            for j in range(W):
                if grid[i][j] == "o":
                    new_grid = [row[:] for row in grid]
                    for ni, nj in get_adjacent_cells(H, W, i, j):
                        new_grid[ni][nj] = "."
                    if not dfs(H, W, new_grid, S_i, S_j, T_i, T_j, set()):
                        min_removed += 1
        return min_removed


H, W = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(H)]
print(min_leaves_to_remove(H, W, grid))
