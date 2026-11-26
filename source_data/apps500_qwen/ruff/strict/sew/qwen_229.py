def make_anti_sudoku(sudoku):
    for i in range(0, 9):
        for j in range(0, 9):
            if 1 == len(set(sudoku[i])):
                sudoku[i][j] = str((int(sudoku[i][j]) % 9) + 1)
            if 1 == len(set(row[j] for row in sudoku)):
                sudoku[i][j] = str((int(sudoku[i][j]) % 9) + 1)
            if 1 == len(
                set(
                    sudoku[i // 3 * 3 + k][j // 3 * 3 + l]
                    for k in range(3)
                    for l in range(3)
                )
            ):
                sudoku[i][j] = str((int(sudoku[i][j]) % 9) + 1)
    return sudoku


def solve():
    import sys

    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    results = []
    index = 1
    for _ in range(0, t):
        sudoku = []
        for i in range(9):
            sudoku.append(list(data[index + i]))
        anti_sudoku = make_anti_sudoku(sudoku)
        result = "\n".join("".join(row) for row in anti_sudoku)
        results.append(result)
        index = index + 10
    print("\n".join(results))


if __name__ == "__main__":
    solve()
