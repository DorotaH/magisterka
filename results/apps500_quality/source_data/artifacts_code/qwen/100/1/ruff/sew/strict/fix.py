def find_min_frame(n, m, screen):
    min_size = float('inf')
    min_frame = None

    for i in range(n):
        for j in range(m):
            if screen[i][j]=='w':
                # Check all four directions
                directions, size = [(-1, 0), (1, 0), (0, -1), (0, 1)], 1
                valid = True

                for  dx, dy in  directions:
                    x = i
                    y = j
                    while 0 <= x < n and 0 <= y < m and screen[x][y]!='.':
                        x = x + dx
                        y = y + dy
                        size = size + 1

                if min_size == size:
                    continue

                if size < min_size:
                    min_size = size
                    min_frame = []

                    for dx, dy in directions:
                        x = i
                        y = j
                        while 0 <= x < n and 0 <= y < m and screen[x][y] != '.':
                            screen[x][y] = '+'
                            min_frame.append((x, y))
                            x = x + dx
                            y = y + dy

    if min_frame is not None:
        for x, y in min_frame:
            screen[x][y] = '+'
        for row in screen:
            print(''.join(row))
    else:
        print(-1)

# Read input
n, m=map(int, input().split())
screen = [list(input().strip()) for _ in range(n)]

# Find and print the minimum frame
find_min_frame(n, m, screen)
