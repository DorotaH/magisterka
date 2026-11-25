n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

min_size = float("inf")
min_frame = None
min_frame_x = None
min_frame_y = None

for y in range(n):
    for x in range(m):
        if grid[y][x] == "w":
            size = 1
            while size <= min_size:
                frame = []
                for i in range(y - size, size + y + 1):
                    frame.extend(
                        (
                            "".join(
                                [
                                    (grid[i][x - size] if i - size >= 0 else " "),
                                    (
                                        grid[i][x - size + 1 : size + x]
                                        if x - size + 1 >= 0
                                        else (" " * abs(x - size))
                                    ),
                                    (
                                        grid[i][size + x + 1]
                                        if i + size + 1 < n
                                        else " "
                                    ),
                                ]
                            ),
                            "".join(
                                [
                                    (grid[i - size][x] if i - size >= 0 else " "),
                                    (
                                        grid[i - size + 1 : x]
                                        if i - size + 1 >= 0
                                        else (abs(i - size) * " ")
                                    ),
                                    grid[i + 1][x] if i + 1 < n else " ",
                                ]
                            ),
                        )
                    )
                if any("w" in row for row in frame) and all(
                    row == "+" for row in frame[:-2]
                ):
                    min_size = size
                    min_frame = frame
                    min_frame_x = x
                    min_frame_y = y
                size += 1

if min_frame is None:
    print(-1)
else:
    for i in range(len(min_frame)):
        print("".join(min_frame[i]))
