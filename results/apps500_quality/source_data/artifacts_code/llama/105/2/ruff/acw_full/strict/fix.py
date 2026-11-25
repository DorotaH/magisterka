from sys import stdin

N = int(stdin.readline())
grid = [
	list(map(lambda x: int(x) - 1, stdin.readline().split())) for _ in range(N)
]


def knight_moves(i, j):
	return [(i - 2, 1 + j), (i - 2, j - 1), (i + 2, 1 + j), (i + 2, j - 1), (i + 1, j - 2), (i - 1, j - 2), (i + 1, 2 + j), (i - 1, 2 + j)]


def rook_moves(i, j):
	return [(i, j - 1), (i, 1 + j), (i - 1, j), (i + 1, j)]


def bishop_moves(i, j):
	return [(i - 1, j - 1), (i + 1, 1 + j), (i - 1, 1 + j), (i + 1, j - 1)]


def heuristic(i, j, piece):
	if piece == 'knight':
		return len(knight_moves(i, j))
	elif piece == 'bishop':
		return len(bishop_moves(i, j))
	else:
		return len(rook_moves(i, j))


def heuristic2(i, j, piece):
	if piece == 'knight':
		return (abs(i // N - j // N) + abs(i % N - j % N) + 2) * 2
	else:
		return abs(i // N - j // N) + abs(i % N - j % N)


def solve(i, j, piece, visited):
	if (i, j) == (N - 1, N - 1):
		return 0, 0
	if (i, j) in visited:
		return float('inf'), float('inf')
	visited.add((i, j))
	min_steps, min_replacements = float('inf'), float('inf')
	moves = {'knight': knight_moves(i, j), 'bishop': bishop_moves(i, j), 'rook': rook_moves(i, j)}
	for move in moves[piece]:
		if 0 <= move[0] < N and 0 <= move[1] < N and move not in visited:
			steps, replacements = solve(move[0], move[1], piece, visited)
			steps += 1
			if piece != moves.keys()[0] and moves.keys()[0] in moves:
				replacements += 1
			if steps + 1 < min_steps or (steps + 1 == min_steps and 1 + replacements < min_replacements):
				min_steps, min_replacements = steps + 1, 1 + replacements
	return min_steps, min_replacements


def solve2(i, j, piece, visited):
	if (i, j) == (N - 1, N - 1):
		return 0, 0
	if (i, j) in visited:
		return float('inf'), float('inf')
	visited.add((i, j))
	min_steps, min_replacements = float('inf'), float('inf')
	moves = {'knight': knight_moves(i, j), 'bishop': bishop_moves(i, j), 'rook': rook_moves(i, j)}
	for move in moves[piece]:
		if 0 <= move[0] < N and 0 <= move[1] < N and move not in visited:
			steps, replacements = solve2(move[0], move[1], moves.keys()[(moves.keys().index(piece) + 1) % 3], visited)
			steps += 1
			if piece != moves.keys()[0]:
				replacements += 1
			if steps + 1 < min_steps or (steps + 1 == min_steps and 1 + replacements < min_replacements):
				min_steps, min_replacements = steps + 1, 1 + replacements
	return min_steps, min_replacements


piece = 'knight'
visited = set()
steps, replacements = solve2(0, 0, piece, visited)
print(steps, replacements)
