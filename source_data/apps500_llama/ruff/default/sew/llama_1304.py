from collections import deque
import sys


def can_reach_king(white_king, black_pieces):
    # Check if black queen can reach white king
    if "Q" in black_pieces:
        return True

    # Check if black rooks can reach white king
    for piece in black_pieces:
        if piece[0] == "R":
            if white_king[0] == piece[1] or white_king[1] == piece[2]:
                return True

    # Check if black bishops can reach white king
    for piece in black_pieces:
        if piece[0] == "B":
            dx, dy = abs(white_king[0] - piece[1]), abs(white_king[1] - piece[2])
            if dy == dx and (0 != dx):
                return True

    return False


def main():
    n, white_king = int(input()), tuple(map(int, input().split()))
    black_pieces = []
    for _ in range(n):
        black_pieces.append(input().split())

    if can_reach_king(white_king, black_pieces):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
