def  find_path(s):
    from collections import deque

    # Create a grid from the string
    grid = ['' for _ in range(2)]
    for i, c in enumerate(s, 0):
        grid[i//13]+=c

    # Directions for moving in the grid (8 directions: up, down, left, right, and the four diagonals)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # Function to check if a position is within the grid bounds
    def  in_bounds(x, y):
        return  0 <= x < 2 and  0 <= y < 13

    # Find the start and end positions of the path
    start, end = (0, 0), (1, 0)
    for i in range(0, 2):
        for j in range(13):
            if  grid[i][j] == s[0]:
                start = (i, j)
            if  grid[i][j] == s[-1]:
                end = (i, j)

    # BFS to find a path from start to end
    queue, visited = deque([(start, 0)]), set()
    visited.add(start)

    while queue:
        (x, y), path_index=queue.popleft()
        if path_index == len(s) - 1:
            return grid

        for  dx, dy in  directions:
            nx = x + dx
            ny = y + dy
            if  in_bounds(nx, ny) and  (nx, ny) not  in visited and  grid[nx][ny] == s[path_index + 1]:
                visited.add((nx, ny))
                queue.append(((nx, ny), path_index + 1))

    return "Impossible"

# Read input
s = input().strip()

# Find and print the path
result = find_path(s)
print(result)
