

def can_win():
	h, n = map(int, input().split())
	moves = list(map(int, input().split()))

	# Sort moves in descending order
	moves.sort(reverse=True)

	used = []
	for move in moves:
		if h >= move:
			used.append(move)
			h -= move
			break
		elif h % move == 0:
			h -= move
		else:
			h -= move - (h % move)

	if h <= 0:
		print('Yes')
	else:
		print('No')


can_win()
