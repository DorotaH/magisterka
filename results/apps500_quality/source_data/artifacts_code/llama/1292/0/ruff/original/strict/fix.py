from collections import deque


def find_player(x, y, grid, n, m, speeds):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == str(x + 1):
                return (i, j)

def expand_player(grid, i, j, speed, n, m, players):
    queue = deque([(i, j)])
    visited = {(i, j)}
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.' and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                grid[nx][ny] = str(players[(nx, ny)])

def main():
    n, m, p = map(int, input().split())
    speeds = list(map(int, input().split()))
    grid = [list(input().strip()) for _ in range(n)]

    players = {(i, j): x for i in range(n) for j in range(m) if (x := grid[i][j]) != '.'}

    while True:
        new_players = players.copy()
        for player, _ in players:
            expand_player(grid, player[0], player[1], speeds[players[player] - 1], n, m, players)
        for player, _ in players:
            if grid[player[0]][player[1]] != str(players[player]):
                new_players.pop(player)
        if new_players == players:
            break
        players = new_players

    result = [0] * p
    for player in players:
        result[players[player] - 1] += 1

    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
