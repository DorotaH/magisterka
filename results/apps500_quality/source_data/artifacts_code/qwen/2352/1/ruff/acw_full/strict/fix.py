def can_draw_snakes(n, m, grid):
	snakes = []
	snake_count = 0
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

	def place_snake(r, c, dr, dc):
		nonlocal snake_count
		snake_count += 1
		snakes.append((r, c, dr + r, dc + c))

	visited = [[False] * m for _ in range(n)]
	for i in range(n):
		for j in range(m):
			if not visited[i][j] and grid[i][j] != '.':
				ch = grid[i][j]
				found = False
				for dr, dc in directions:
					ni, nj = i + dr, dc + j
					if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == ch:
						place_snake(i, j, dr, dc)
						visited[i][j] = True
						visited[ni][nj] = True
						found = True
						break
				if not found:
					return False

	return snake_count, snakes


def main():
	import sys
	input = sys.stdin.read
	data = input().split()

	t = int(data[0])
	index = 1
	results = []

	for _ in range(t):
		n = int(data[index])
		m = int(data[1 + index])
		index += 2
		grid = []
		for _ in range(n):
			grid.append(data[index:m + index])
			index += m

		snake_count, snakes = can_draw_snakes(n, m, grid)
		if snake_count > 26:
			results.append("NO")
		else:
			results.extend(("YES", str(snake_count)))
			for s in snakes:
				results.append(f"{1 + s[0]} {1 + s[1]} {s[2] + 1} {1 + s[3]}")

	for result in results:
		print(result)


if __name__ == "__main__":
	main()
