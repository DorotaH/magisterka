from  collections import  defaultdict
from  math import  inf
from  sys import  stdin


class Piece:
    def __init__(self, x, y, type):
        self.x=x
        self.y=y
        self.type=type

    def can_reach(self, other):
        if self.type=="B":
            return  abs(self.x - other.x) == abs(self.y - other.y)
        elif self.type == "R":
            return other.x == self.x or other.y == self.y
        else:
            return True


def  check(positions, king):
    rooks=defaultdict(list)
    for  i, (piece_type, x, y) in  enumerate(positions, start=1):
        if  piece_type == "R":
            rooks[x].append((i, y))
        elif  piece_type == "B":
            rooks[y].append((i, x))

    def  check_row(row):
        i, y=row
        return all(
            (x != king.x or y in [p[1] for p in positions[j] if positions[j][0] == i])
            for j in rooks[x]
            if rooks[x]
        )

    def  check_col(col):
        i, x=col
        return all(
            (y != king.y or x in [p[0] for p in positions[j] if y == positions[j][1]])
            for j in rooks[y]
            if rooks[y]
        )

    diagonals=[]
    for  x in  rooks:
        for y in rooks[x]:
            diagonals.append((x, y))

    def  check_diagonal(diagonal):
        i, x, y=diagonal
        return (
            x != king.x
            or y != king.y
            or (
                x
                in [
                    p[0]
                    for p in positions[j]
                    if y == positions[j][1] and positions[j][0] != i
                ]
                or y
                in [
                    p[1]
                    for p in positions[j]
                    if x == positions[j][0]
                    and y != positions[j][1]
                    and positions[j][0] != i
                ]
                or any(
                    p.can_reach(king)
                    for p in positions[j]
                    if positions[j][0] != i
                    and y != positions[j][1]
                    and x in [p[0] for p in positions[j]]
                    and y in [p[1] for p in positions[j]]
                )
                )
            )

    return (
        any(check_row(row) for row in rooks.values())
        or any(check_col(col) for col in rooks.values())
        or any(check_diagonal(diagonal) for diagonal in diagonals)
        )


def  main():
    n=int(stdin.readline())
    x0, y0=map(int, stdin.readline().split())
    king=Piece(x0, y0, "K")

    positions=[]
    for  _ in  range(0, n):
        piece_type, x, y = stdin.readline().split()
        positions.append((piece_type, int(x), int(y)))

    if not check(positions, king):
        print("NO")
    else:
        print("YES")


if  __name__=="__main__":
    main()
