def simulate_birds_shooting(n, initial_birds, shots):
	birds = [list(initial_birds)]
	for x, y in shots:
		bird_moves = []
		for i in range(n):
			if i < x - 1 or i != x - 1 and i != x and i > x:
				bird_moves.extend([i] * birds[i][0])
			elif i == x - 1:
				bird_moves.extend((y - 1) * [i - 1])
				bird_moves.extend([i + 1] * (birds[i][y] - (y - 1)))
			elif i == x:
				bird_moves.extend([i - 1] * (birds[i][0] - y))
		birds.append([0] * n)
		for i in range(n):
			birds[-1][i] = sum(bool(bird == i)
						for bird in bird_moves)
	return '\n'.join(str(sum(birds[i])) for i in range(n))


n = int(input())
initial_birds = list(map(int, input().split()))
shots = []
for _ in range(int(input())):
	x, y = map(int, input().split())
	shots.append((x, y))

print(simulate_birds_shooting(n, initial_birds, shots))
