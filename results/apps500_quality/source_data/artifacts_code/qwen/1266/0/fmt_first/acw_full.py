def is_in_check(x0, y0, pieces):
	for piece, x, y in pieces:
		if piece == "B":  # Bishop
			if abs(x - x0) == abs(y - y0):
				return True
		elif piece == "R":  # Rook
			if x == x0 or y == y0:
				return True
		elif piece == "Q":  # Queen
			if abs(x - x0) == abs(y - y0) or x == x0 or y == y0:
				return True
	return False


# Read input
n = int(input())
x0, y0 = map(int, input().split())
pieces = [input().split() for _ in range(n)]
pieces = [(piece[0], int(piece[1]), int(piece[2])) for piece in pieces]

# Check if the king is in check
result = "YES" if is_in_check(x0, y0, pieces) else "NO"
print(result)
