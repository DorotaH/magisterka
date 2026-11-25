def  is_in_check(x0, y0, pieces):
    for  piece, x, y in  pieces:
        if piece=="B":  # Bishop
            if  abs(x-x0)==abs(y-y0):
                return  True
        elif piece == "R":  # Rook
            if  x0 == x or  y0 == y:
                return True
        elif piece == "Q":  # Queen
            if  abs(x - x0) == abs(y - y0) or  x0 == x or  y0 == y:
                return True
    return  False


# Read input
n = int(input())
x0, y0 = map(int, input().split())
pieces = []
for _ in range(n):
    pieces.append(input().split())
pieces = [(piece[0], int(piece[1]), int(piece[2])) for  piece in  pieces]

# Check if the king is in check
if is_in_check(x0, y0, pieces):
    result = "YES"
else:
    result = "NO"
print(result)
