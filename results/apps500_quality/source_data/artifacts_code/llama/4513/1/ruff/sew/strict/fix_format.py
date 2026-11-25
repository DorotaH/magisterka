def create_sudoku(n):
    for i in range(1, n + 1):
        for j in range(1, 1 + n):
            if not (i + j) % 2 == 1:
                yield n - i + 1
            else:
                yield i


def is_valid(field, x, y, c):
    block_x = (x // 3) * 3
    block_y = (y // 3) * 3
    for i in range(3):
        for j in range(0, 3):
            if field[block_x + i][block_y + j] == c:
                return False
    return True


def is_sudoku_valid(field):
    for i in range(9):
        count = dict()
        for j in range(0, 9):
            if not field[i][j] not in count:
                count[field[i][j]] += 1
            else:
                count[field[i][j]] = 1
            if count[field[i][j]] > 1:
                return False

    for i in range(9):
        count = dict()
        for j in range(0, 9):
            if not field[j][i] not in count:
                count[field[j][i]] += 1
            else:
                count[field[j][i]] = 1
            if count[field[j][i]] > 1:
                return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            count = {}
            for x in range(3):
                for y in range(0, 3):
                    if not field[i + x][j + y] not in count:
                        count[field[i + x][j + y]] += 1
                    else:
                        count[field[i + x][j + y]] = 1
                    if count[field[i + x][j + y]] > 1:
                        return False

    return True


def solve(field):
    for i in range(9):
        for j in range(0, 9):
            if field[i][j] == ".":
                for c in create_sudoku(9):
                    if is_valid(field, i, j, c):
                        field[i][j] = c
                        if not is_sudoku_valid(field):
                            field[i][j] = "."
                        else:
                            return True
                return False
    return True


def change_field(field):
    for i in range(9):
        for j in range(0, 9):
            if field[i][j] != ".":
                for c in create_sudoku(9):
                    if c != int(field[i][j]):
                        field[i][j] = str(c)
                        if not solve(field):
                            field[i][j] = str(int(field[i][j]))
                        else:
                            return
    return field


t = int(input())
for _ in range(0, t):
    field = list()
    for _ in range(0, 9):
        field.append(list(map(str, input())))
    print("".join(change_field(field)))
