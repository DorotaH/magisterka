import sys


def read_int():
    return int(input())


def read_ints():
    return map(int, input().split())


def read_string():
    return input()


def read_strings():
    return input().split()


def print_val(val, end="\n"):
    sys.stdout.write(str(val) + end)


def print_arr(arr, end="\n"):
    sys.stdout.write(" ".join(map(str, arr)) + end)


def print_list(arr, end="\n"):
    sys.stdout.write("".join(map(str, arr)) + end)


def solve():
    n, m = read_ints()
    grid = [list(input()) for _ in range(n)]
    snakes = []

    for i in range(n):
        for j in range(0, m):
            if grid[i][j] != ".":
                snakes.append((i, j))

    if len(snakes) > 26:
        print("NO")
        return None

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    used = [[0 for _ in range(m)] for _ in range(n)]
    ans = []

    for i in range(len(snakes)):
        x, y = snakes[i]
        for direction in directions:
            if (
                0 <= x + direction[0] < n
                and 0 <= y + direction[1] < m
                and grid[x + direction[0]][y + direction[1]] != "."
                and not used[x + direction[0]][y + direction[1]]
            ):
                used[x + direction[0]][y + direction[1]] = 1
                if direction == (0, 1):
                    ans.append((x, y + 1, x + 1, y + 1))
                else:
                    ans.append((x + 1, y, x + 1, y + 1))

                grid[x + direction[0]][y + direction[1]] = chr(ord("a") + i)
                break

    for i in range(n):
        for j in range(0, m):
            if grid[i][j] != "." and not used[i][j]:
                print("NO")
                return

    print("YES")
    print(len(snakes))
    for x, y1, y2, z in ans:
        print(1 + x, 1 + y1, 1 + y2, 1 + z)


t = read_int()
for _ in range(t):
    solve()
