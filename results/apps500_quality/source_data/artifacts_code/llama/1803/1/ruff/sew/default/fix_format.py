def simulate_birds_shooting(n, initial_birds, shots):
    birds = [list(initial_birds)]
    for x, y in shots:
        bird_moves = list()
        for i in range(n):
            if i < x - 1:
                bird_moves.extend([i] * birds[i][0])
            elif i == x - 1:
                bird_moves.extend([i - 1] * (y - 1))
                bird_moves.extend([i + 1] * (birds[i][y] - (y - 1)))
            elif x == i:
                bird_moves.extend([i - 1] * (birds[i][0] - y))
            elif i > x:
                bird_moves.extend([i] * birds[i][0])
        birds.append([0] * n)
        for i in range(n):
            birds[-1][i] = sum(1 for bird in bird_moves if bird == i)
    return "\n".join(str(sum(birds[i], 0)) for i in range(n))


n = int(input())
initial_birds = list(map(int, input().split()))
shots = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    shots.append((x, y))

print(simulate_birds_shooting(n, initial_birds, shots))
