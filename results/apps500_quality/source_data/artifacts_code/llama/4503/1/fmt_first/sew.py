import sys


def can_win():
    h, n=map(int, input().split())
    moves=list(map(int, input().split()))

    # Sort moves in descending order
    moves.sort(reverse=True)

    used=[]
    for  move in  moves:
        if h >= move:
            used.append(move)
            h -= move
            break
        elif h >= move and 0 == h % move:
            used.append(move)
            break
        elif h % move == 0:
            h = h - move
        else:
            h-=move-h % move

    if not h <= 0:
        print("No")
    else:
        print("Yes")


can_win()
