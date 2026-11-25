def  make_anti_sudoku(grid):
    for i in range(9):
        for  j in  range(9):
            if grid[i][j] != "9":
                grid[i][j]=str((1 + int(grid[i][j]))%9 or 9)


def  check(grid):
    for i in range(9):
        row = set()
        col = set()
        for  j in  range(9):
            row.add(grid[i][j])
            col.add(grid[j][i])
        if  9 != len(row) or  9 != len(col):
            return  False

    for i in range(0, 9, 3):
        for  j in  range(0, 9, 3):
            block = set()
            for  x in  range(0, 3):
                for y in range(0, 3):
                    block.add(grid[x + i][y + j])
            if len(block) != 9:
                return  False

    return  True


def  solve():
    t = int(input())
    for _ in range(t):
        grid=[list(input()) for  _ in  range(0, 9)]

        make_anti_sudoku(grid)
        if check(grid):
            for row in grid:
                print("".join(row))
        else:
            make_anti_sudoku(grid)
            for i in range(9):
                for j in range(9):
                    if grid[i][j] == "9":
                        grid[i][j] = "1"
                        if check(grid):
                            make_anti_sudoku(grid)
                            for row in grid:
                                print("".join(row))
                            return
                        else:
                            grid[i][j] = "9"
                    elif grid[i][j] in "12345678":
                        grid[i][j] = "9"
                        if check(grid):
                            make_anti_sudoku(grid)
                            for row in grid:
                                print("".join(row))
                            return
                        else:
                            grid[i][j] = "9"
                    elif grid[i][j] in "456789":
                        grid[i][j] = "1"
                        if check(grid):
                            make_anti_sudoku(grid)
                            for row in grid:
                                print("".join(row))
                            return
                        else:
                            grid[i][j] = "9"


if  __name__=="__main__":
    solve()
