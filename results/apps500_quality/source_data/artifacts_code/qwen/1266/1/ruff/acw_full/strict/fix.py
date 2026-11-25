def is_king_in_check(king_x, king_y, pieces):
	for piece_type, x, y in pieces:
		if piece_type in ['Q', 'R']:
			if x == king_x or y == king_y:
				return True
		elif piece_type == 'B':
			if abs(x - king_x) == abs(y - king_y):
				return True
	return False


def main():
	import sys
	input = sys.stdin.read
	data = input().split()

	n = int(data[0])
	king_x, king_y = map(int, data[1:3])

	pieces = []
	for i in range(n):
		piece_type = data[6 + i * 3]
		x = int(data[7 + i * 3])
		y = int(data[8 + i * 3])
		pieces.append((piece_type, x, y))

	if is_king_in_check(king_x, king_y, pieces):
		print("YES")
	else:
		print("NO")


if __name__ == "__main__":
	main()
