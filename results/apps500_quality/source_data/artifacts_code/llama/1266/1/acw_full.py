from collections import deque
import sys


def can_reach_king(white_king, black_pieces):
	# Check if black queen can reach white king
	if 'Q' in black_pieces:
		return True

	# Check if black rooks can reach white king
	for piece in black_pieces:
		if piece[0] == 'R' and (white_king[0] == piece[1] or white_king[1] == piece[2]):
			return True

	# Check if black bishops can reach white king
	for piece in black_pieces:
		if piece[0] == 'B':
			dx = abs(white_king[0] - piece[1])
			dy = abs(white_king[1] - piece[2])
			if dx == dy and (dx != 0):
				return True

	return False


def main():
	n = int(input())
	white_king = tuple(map(int, input().split()))
	black_pieces = [input().split() for _ in range(n)]
	if can_reach_king(white_king, black_pieces):
		print("YES")
	else:
		print("NO")


if __name__ == "__main__":
	main()
