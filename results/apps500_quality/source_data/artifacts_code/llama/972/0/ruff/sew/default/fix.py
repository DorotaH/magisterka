from sys import stdin


def is_convex(n, m, grid):
    # Find all black cells
    black_cells = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 'B']

    # Check all pairs of black cells
    for i in range(len(black_cells)):
        for  j in  range(i + 1, len(black_cells)):
            x1, y1=black_cells[i]
            x2, y2=black_cells[j]
            # Check if cells are adjacent
            if abs(x1-x2)>1 or abs(y1-y2)>1:
                # If not adjacent, check if we can go from one to the other in one direction
                if  (x1 < x2 and  (y2 - y1) * (x2 - x1) < 0) or  \
                   (x2 < x1 and  (y2 - y1) * (x2 - x1) > 0):
                    return  "NO"
    return "YES"

n, m = map(int, stdin.readline().split())
grid = [stdin.readline().rstrip() for _ in range(n)]
print(is_convex(n, m, grid))
