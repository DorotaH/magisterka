def make_anti_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            if len(set(sudoku[i])) == 1:
                sudoku[i][j] = str((int(sudoku[i][j]) % 9) + 1)
            if len(set(row[j] for row in sudoku)) == 1:
                sudoku[i][j] = str((int(sudoku[i][j]) % 9) + 1)
            if len(set(sudoku[i//3*3+k][j//3*3+l] for k in range(3) for l in range(3))) == 1:
                sudoku[i][j] = str((int(sudoku[i][j]) % 9) + 1)
    return sudoku

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    results = []
    index = 1
    for _ in range(t):
        sudoku = [list(data[index + i]) for i in range(9)]
        anti_sudoku = make_anti_sudoku(sudoku)
        result = '\n'.join(''.join(row) for row in anti_sudoku)
        results.append(result)
        index += 10
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
