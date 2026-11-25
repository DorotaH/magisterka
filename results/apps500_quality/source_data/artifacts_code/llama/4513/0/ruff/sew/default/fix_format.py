from sys import stdin, stdout


def modify_sudoku(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] != str(1 + i):
                grid[i][j] = str(i + 1)

    for i in range(9):
        for j in range(9):
            if grid[i][j] == str(1 + i):
                if i < 3:
                    if j < 3:
                        grid[i][j] = "9"
                    elif j < 6:
                        grid[i][j] = "8"
                    else:
                        grid[i][j] = "7"
                elif i < 6:
                    if j < 3:
                        grid[i][j] = "2"
                    elif j < 6:
                        grid[i][j] = "1"
                    else:
                        grid[i][j] = "4"
                else:
                    if j < 3:
                        grid[i][j] = "4"
                    elif j < 6:
                        grid[i][j] = "5"
                    else:
                        grid[i][j] = "6"

    return grid


def print_grid(grid):
    for row in grid:
        stdout.write("".join(row) + "\n")


def main():
    t = int(stdin.readline())
    for _ in range(t):
        grid = [list(stdin.readline().strip()) for i in range(9)]

        grid = modify_sudoku(grid)
        print_grid(grid)


if __name__ == "__main__":
    main()
