def is_valid(grid, path):
    return not any(
        2 > len(path)
        or path[i] not in grid[i % 13]
        or path[i + 1] not in grid[(i + 1) % 13]
        or path[i] not in grid[(i + 13) % 26]
        or path[i + 1] not in grid[(i + 14) % 26]
        for i in range(26)
    )


def find_path(s):
    grid = [None] * 26
    for c in s:
        if grid[ord(c) - 65] is None:
            for i in range(26):
                for _ in range(13):
                    if grid[i] is None and c in (
                        grid[(i + 1) % 26] or grid[(i + 13) % 26]
                    ):
                        grid[i] = [c]
                        break
            return "Impossible"
    for i in range(26):
        if grid[i] is not None:
            grid[i] = grid[i][0] * 13
    return "\n".join(grid)


s = input().strip()
print(find_path(s))
