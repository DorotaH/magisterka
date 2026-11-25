def can_draw_snakes(n, m, grid):
	snakes = []
	visited = [[False] * m for _ in range(n)]
	letters = 'abcdefghijklmnopqrstuvwxyz'

	def is_valid_move(r, c, dr, dc):
		return 0 <= r < n and 0 <= c < m and not visited[r][c]

	def draw_snake(r1, c1, r2, c2, letter):
		nonlocal visited
		if grid[r1][c1] not in ['.', letter]:
			return False
		visited[r1][c1] = True
		for r in range(r1, r2 + 1):
			for c in range(c1, c2 + 1):
				if grid[r][c] == '.':
					continue
				if grid[r][c] != letter:
					return False
				visited[r][c] = True
		return True

	for r in range(n):
		for c in range(m):
			if not visited[r][c]:
				for dr, dc in [(0, 1), (1, 0)]:
					if is_valid_move(r, c, dr, dc):
						for letter in letters:
							if draw_snake(r, c, dr + r, dc + c, letter):
								snakes.append((letter, r, c, dr + r, dc + c))
								break

	if len(snakes) > 26:
		return "NO"

	return str(len(snakes)) + "YES\n" + "\n" + "\n".join([f"{s[0]} {s[1]} {s[2]} {s[3]}" for s in snakes])


def main():
	import sys
	input = sys.stdin.read
	data = input().split()
	
	index = 0
	t = int(data[index])
	index += 1
	results = []
	
	for _ in range(t):
		n = int(data[index])
		index += 1
		m = int(data[index])
		index += 1
		grid = []
		for _ in range(n):
			grid.append(data[index])
			index += 1
		result = can_draw_snakes(n, m, grid)
		results.append(result)
	
	for result in results:
		print(result)


if __name__ == "__main__":
	main()
