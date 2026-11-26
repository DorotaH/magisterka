def is_king_in_check(n, king_x, king_y, pieces):
    for piece_type, x, y in pieces:
        if piece_type in ["Q", "B"]:
            if abs(x - king_x) == abs(y - king_y):  # Diagonal attack
                return True
        elif piece_type in ["Q", "R"]:
            if x == king_x or y == king_y:  # Horizontal or vertical attack
                return True
    return False


# Read input
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
king_x, king_y = int(data[1]), int(data[2])
pieces = []
for i in range(n):
    piece_type = data[3 + i * 3]
    x = int(data[4 + i * 3])
    y = int(data[5 + i * 3])
    pieces.append((piece_type, x, y))

# Check if the king is in check
result = "YES" if is_king_in_check(n, king_x, king_y, pieces) else "NO"
print(result)
