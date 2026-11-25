def can_draw_snakes(n, m, grid):
    # Check if the grid can be formed by drawing snakes
    visited = [[False] * m for _ in range(n)]
    snake_count = 0
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    def is_valid_snake(r1, c1, r2, c2):
        if r1 == r2:
            if c1 > c2:
                c1, c2 = c2, c1
            for c in range(c1, c2 + 1):
                if grid[r1][c] != '.' and grid[r1][c] != letters[snake_count]:
                    return False
            return True
        elif c1 == c2:
            if r1 > r2:
                r1, r2 = r2, r1
            for r in range(r1, r2 + 1):
                if grid[r][c1] != '.' and grid[r][c1] != letters[snake_count]:
                    return False
            return True
        return False
    
    for r in range(n):
        for c in range(m):
            if grid[r][c] != '.' and not visited[r][c]:
                if is_valid_snake(r, c, r, c + 1):
                    visited[r][c:c + 1] = [True] * (c + 1 - c)
                    snake_count += 1
                elif is_valid_snake(r, c, r + 1, c):
                    visited[r:r + 1][c] = [True] * (r + 1 - r)
                    snake_count += 1
                else:
                    return False
    
    return snake_count

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        grid = data[index:index + n]
        index += n
        
        if can_draw_snakes(n, m, grid):
            results.append('YES')
            results.append(str(can_draw_snakes(n, m, grid)))
            for r in range(n):
                for c in range(m):
                    if grid[r][c] != '.' and grid[r][c] != 'a':
                        if c + 1 < m and grid[r][c] == grid[r][c + 1]:
                            results.append(f"{r + 1} {c + 1} {r + 1} {c + 2}")
                        elif r + 1 < n and grid[r][c] == grid[r + 1][c]:
                            results.append(f"{r + 1} {c + 1} {r + 2} {c + 1}")
        else:
            results.append('NO')
    
    return '\n'.join(results)

print(solve())
