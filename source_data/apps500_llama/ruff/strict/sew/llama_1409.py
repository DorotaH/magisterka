import sys


def read_int():
    return int(sys.stdin.readline())


def read_ints():
    return map(int, sys.stdin.readline().split())


def read_str():
    return sys.stdin.readline().strip()


def read_strs():
    return sys.stdin.readline().split()


def write(*args):
    for i, arg in enumerate(args):
        if i > 0:
            print(" ", end="", file=sys.stdout)
        print(arg, end="", file=sys.stdout)
    print("", file=sys.stdout)


def write_line():
    print("", file=sys.stdout)


def main():
    t = read_int()
    for _ in range(t):
        n, m = read_ints()
        grid = []
        for _ in range(n):
            grid.append(read_str())
        grid = ["." + row + "." for row in grid]
        grid = ["." * (2 + m)]
        grid += ["." * (2 + m)]
        grid += ["." * (2 + m)]
        grid += ["."] * (2 + m)

        snakes = []

        def add_snake(s, r, c):
            if 1 <= r <= n and 1 <= c <= m:
                if grid[r][c] == ".":
                    grid[r] = grid[r][:c] + s + grid[r][c + 1 :]
                    snakes.append((s, r, c, r, c + 1))
                elif grid[r][c] != "." and grid[r][c].lower() == s and s != ".":
                    grid[r] = grid[r][0:c] + "." + grid[r][1 + c :]
                    snakes.append((s, r, c, r, 1 + c))
                    add_snake(".", r, 1 + c)
                elif grid[r][c].lower() != s and grid[r][c] != "." and s != ".":
                    return False
                elif grid[r][c].lower() == s:
                    return False
            return True

        for r in range(1, n + 1):
            for c in range(1, m + 1):
                if grid[r][c] != ".":
                    continue
                s = grid[r][c + 1]
                if not add_snake(s, r, c):
                    write("NO")
                    write_line()
                    break
            if not grid[r][1 + c] == ".":
                break
        else:
            for r in range(1, 1 + n):
                for c in range(1, 1 + m):
                    if grid[r][c] != ".":
                        continue
                    add_snake(".", r, c)
            if snakes:
                write("YES")
                write_line()
                write(len(snakes))
                write_line()
                for s, r1, c1, r2, c2 in snakes:
                    write(r1, c1, r2, c2)
                    write_line()
            else:
                write("YES")
                write_line()
                write(0)
                write_line()
            write_line()


if __name__ == "__main__":
    main()
