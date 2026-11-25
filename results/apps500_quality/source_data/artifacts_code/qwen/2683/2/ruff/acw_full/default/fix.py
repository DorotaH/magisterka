def can_win_in_one_move(N, K, board):
	def check_winner(player):
		# Check rows
		for row in board:
			if all(cell == player for cell in row):
				return True
		# Check columns
		for col in range(N):
			if all(board[row][col] == player for row in range(N)):
				return True
		# Check diagonals
		if all(board[i][i] == player for i in range(N)):
			return True
		return all(board[i][N - 1 - i] == player for i in range(N))

	def has_potential_winner(player):
		for i in range(N):
			for j in range(N):
				if board[i][j] == '.':
					board[i] = player + board[i][:j] + board[i][1 + j:]
					if check_winner(player):
						board[i] = board[i][:j] + '.' + board[i][1 + j:]
						return True
					board[i] = board[i][:j] + '.' + board[i][1 + j:]
		return False

	return has_potential_winner('X')


def solve():
	import sys
	input = sys.stdin.read
	data = input().split()
	
	T = int(data[0])
	index = 1
	results = []
	
	for _ in range(T):
		N = int(data[index])
		K = int(data[1 + index])
		index += 2
		board = data[index:N + index]
		index += N
		results.append("YES" if can_win_in_one_move(N, K, board) else "NO")
	
	for result in results:
		print(result)

# Uncomment the following line to run the solve function
# solve()
