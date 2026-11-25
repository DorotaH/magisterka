def make_anti_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            if (
                len(
                    set(sudoku[i][j * 3 : (j + 1) * 3] + sudoku[j][i * 3 : (i + 1) * 3])
                )
                == 9
            ):
                if sudoku[i][j] == "9":
                    sudoku[i] = sudoku[i][:j] + "8" + sudoku[i][j + 1 :]
                else:
                    sudoku[i] = (
                        sudoku[i][:j] + str(int(sudoku[i][j]) + 1) + sudoku[i][j + 1 :]
                    )
    return sudoku


def main():
    import sys

    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    results = []
    for i in range(t):
        sudoku = data[1 + 9 * i : 1 + 9 * (i + 1)]
        anti_sudoku = make_anti_sudoku(sudoku)
        results.append("\n".join(anti_sudoku))
    print("\n".join(results))


if __name__ == "__main__":
    main()
