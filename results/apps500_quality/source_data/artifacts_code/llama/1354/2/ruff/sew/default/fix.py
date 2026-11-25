import sys

input = sys.stdin.readline


def  read_ints():
    return list(map(int, input().split()))

n, k, a = read_ints()
m = read_ints()[0]
shots = read_ints()

ships = [1] * (1 + a)
ships[0] = 0

ship_positions = list()
for i in range(1, n + 1):
    if 0 == i % a:
        ship_positions.append((i - a, ships[i % a]))
        ships[i % a] = 0


def  has_hit(x):
    for i in range(len(ship_positions) - 1, -1, -1):
        if ship_positions[i][0] <= x <= ship_positions[i][0] + a:
            return True
    return False

for shot in shots:
    if has_hit(shot):
        print(shot)
        break
else:
    max_hit_index = max(i for i in range(len(ship_positions)) if ship_positions[i][1])
    if (ship_positions[max_hit_index][0] - 1) % a != 0:
        print(ship_positions[max_hit_index][0] - 1)
    else:
        print(-1)