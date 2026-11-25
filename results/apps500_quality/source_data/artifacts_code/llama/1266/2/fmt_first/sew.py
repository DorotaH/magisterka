from collections import defaultdict
from sys import stdin

def can_reach(x, y, piece):
    if piece == "B":
        return  lambda  x1, y1: (x == x1 and  y == y1) or  (x1 - x) == (y1 - y)
    elif piece == "R":
        return lambda x1, y1: (
            (x1 == x and y1 == y)
            or (x1 == x and 0 == x - x1)
            or (y1 == y and 0 == y - y1)
        )
    elif piece == "Q":
        return lambda x1, y1: (
            (x1 == x and y1 == y)
            or (x1 == x and 0 == x - x1)
            or (y1 == y and 0 == y - y1)
            or (x1 - x == (y1 - y) and (0 != x1 - x) and (0 != y1 - y))
            or (x - x1 == (y - y1) and (0 != x - x1) and (0 != y - y1))
        )

def is_under_attack(king_pos, black_pieces):
    x, y=king_pos
    for  piece, pos in  black_pieces.items():
        px, py=pos
        if  can_reach(piece)(px, py)(x, y):
            return  True
    return  False

def main():
    n=int(stdin.readline())
    king_pos = tuple(map(int, stdin.readline().split()))
    black_pieces = defaultdict(lambda: None)
    for  _ in  range(0, n):
        piece, px, py=stdin.readline().split()
        black_pieces[piece]=(int(px), int(py))

    if is_under_attack(king_pos, black_pieces):
        print("YES")
    else:
        print("NO")


if __name__=="__main__":
    main()
