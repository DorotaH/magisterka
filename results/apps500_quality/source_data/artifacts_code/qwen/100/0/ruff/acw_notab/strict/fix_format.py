import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
screen = data[2:]


def find_min_frame(n, m, screen):
    min_size = float("inf")
    min_frame = None
    for i in range(n):
        for j in range(m):
            if screen[i][j] == ".":
                for size in range(1, 1 + min(n - i, m - j)):
                    valid = True
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            if di == 0 and dj == 0:
                                continue
                            ni, nj = i + size * di, j + size * dj
                            if (
                                ni < 0
                                or ni >= n
                                or nj < 0
                                or nj >= m
                                or screen[ni][nj] == "."
                            ):
                                valid = False
                                break
                        if not valid:
                            break
                    if valid:
                        if size < min_size:
                            min_size = size
                            min_frame = (i, j, size)
                        break

    if min_frame is None:
        return "-1"
    result = [list(row) for row in screen]
    i, j, size = min_frame
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == 0 and dj == 0:
                continue
            ni, nj = i + size * di, j + size * dj
            result[ni][nj] = "+"
    return "\n".join(["".join(row) for row in result])


print(find_min_frame(n, m, screen))
