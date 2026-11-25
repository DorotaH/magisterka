

def create_sudoku(n):
    for i in range(1, 1 + n):
        for j in range(1, 1 + n):
            if (i + j) % 2 == 1:
                yield i
            else:
                yield n - i + 1


def is_valid(field, x, y, c):
    block_x = 3 * (x // 3)
    block_y = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if field[i + block_x][block_y + j] == c:
                return False
    return True


def is_sudoku_valid(field):
    for i in range(9):
        count = {}
        for j in range(9):
            if field[i][j] not in count:
                count[field[i][j]] = 1
            else:
                count[field[i][j]] += 1
            if count[field[i][j]] > 1:
                return False

    for i in range(9):
        count = {}
        for j in range(9):
            if field[j][i] not in count:
                count[field[j][i]] = 1
            else:
                count[field[j][i]] += 1
            if count[field[j][i]] > 1:
                return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            count = {}
            for x in range(3):
                for y in range(3):
                    if field[i + x][y + j] not in count:
                        count[field[i + x][y + j]] = 1
                    else:
                        count[field[i + x][y + j]] += 1
                    if count[field[i + x][y + j]] > 1:
                        return False

    return True


def solve(field):
    for i in range(9):
        for j in range(9):
            if field[i][j] == '.':
                for c in create_sudoku(9):
                    if is_valid(field, i, j, c):
                        field[i][j] = c
                        if is_sudoku_valid(field):
                            return True
                        else:
                            field[i][j] = '.'
                return False
    return True


def change_field(field):
    for i in range(9):
        for j in range(9):
            if field[i][j] != '.':
                for c in create_sudoku(9):
                    if c != int(field[i][j]):
                        field[i][j] = str(c)
                        if solve(field):
                            return
                        else:
                            field[i][j] = str(int(field[i][j]))
    return field


t = int(input())
for _ in range(t):
    field = [list(map(str, input())) for _ in range(9)]
    print(''.join(change_field(field)))
