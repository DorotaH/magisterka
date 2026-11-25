def find_min_frame(n, m, screen):
    min_size = float('inf')
    min_frame = None

    for i in range(n):
        for j in range(m):
            if screen[i][j] == 'w':
                # Check all four directions
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                size = 1
                valid = True

                for dx, dy in directions:
                    x, y = i, j
                    while 0 <= x < n and 0 <= y < m and screen[x][y] != '.':
                        x += dx
                        y += dy
                        size += 1

                if size == min_size:
                    continue

                if size < min_size:
                    min_size = size
                    min_frame = []

                    for dx, dy in directions:
                        x, y = i, j
                        while 0 <= x < n and 0 <= y < m and screen[x][y] != '.':
                            screen[x][y] = '+'
                            min_frame.append((x, y))
                            x += dx
                            y += dy

    if min_frame is None:
        print(-1)
    else:
        for x, y in min_frame:
            screen[x][y] = '+'
        for row in screen:
            print(''.join(row))


# Read input
n, m = map(int, input().split())
screen = [list(input().strip()) for _ in range(n)]

# Find and print the minimum frame
find_min_frame(n, m, screen)
