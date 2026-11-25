def solve():
    n, k, a = map(int, input().split())
    m = int(input())
    shots = list(map(int, input().split()))

    ships = [0] * (n + 1)
    for i in range(k):
        ships[(i * a + 1) % n] = 1
        ships[(i * a + a) % n] = 1

    for i in range(1, n + 1):
        ships[i] += ships[i - 1]

    for shot in shots:
        if (ships[shot - 1] - ships[shot - 1 - a] == 1 or
            ships[shot] - ships[shot - 1] == 0 or
            (shots.index(shot) == 0 and ships[shot - 1] - ships[shot - 1 - a] == 0)):
            print(shot)
            return
    print(-1)

solve()
