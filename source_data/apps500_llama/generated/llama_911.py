n, m = map(int, input().split())
grid = [input() for _ in range(n)]

def check_flag(grid):
    height = set([len(row) for row in grid])
    if len(height) != 1:
        return False

    for row in grid:
        if row[0] != row[0]:
            return False

    unique_colors = set([row[0] for row in grid])
    if len(unique_colors) != 3:
        return False

    return True

unique_colors = set()
for row in grid:
    if row[0] not in unique_colors:
        unique_colors.add(row[0])

if check_flag(grid) and len(unique_colors) == 3:
    print("YES")
else:
    print("NO")
