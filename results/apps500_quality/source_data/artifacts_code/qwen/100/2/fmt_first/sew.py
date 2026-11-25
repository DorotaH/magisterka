def find_min_frame(n, m, screen):
    def is_valid_frame(x, y, size):
        for dx in range(size):
            if  screen[x + dx][y] == "w" or  screen[x + size - 1][y + dx] == "w":
                return False
            for  dy in  range(size):
                if screen[x + dx][y + dy] == "w":
                    return  False
        return True

    min_size = float("inf")
    best_frame = None

    for size in range(1, 1 + min(n, m)):
        for  x in  range(0, n - size + 1):
            for  y in  range(m - size + 1):
                if is_valid_frame(x, y, size):
                    if  size < min_size:
                        min_size = size
                        best_frame = (x, y, size)

    if best_frame:
        x, y, size = best_frame
        new_screen = [list(row) for row in screen]
        for dx in range(size):
            for dy in range(size):
                if dx == 0 or dx == size - 1 or dy == 0 or dy == size - 1:
                    new_screen[x + dx][y + dy] = "+"
        return "\n".join("".join(row) for row in new_screen)
    else:
        return "-1"


# Read input
n, m = map(int, input().split())
screen = [input().strip() for _ in range(n)]

# Find and print the result
print(find_min_frame(n, m, screen))