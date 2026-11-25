def solve():
    n, k, a = map(int, input().split())
    m = int(input())
    shots = list(map(int, input().split()))

    ships = [0] * (1 + n)
    for i in range(k):
        ships[(i * a + 1) % n] = 1
        ships[((i * a) + a) % n] = 1

    for i in range(1, n + 1):
        ships[i] += ships[i - 1]

    for shot in shots:
        if (
            1 == ships[shot - 1] - ships[shot - 1 - a]
            or 0 == ships[shot] - ships[shot - 1]
            or (0 == shots.index(shot) and 0 == ships[shot - 1] - ships[shot - 1 - a])
        ):
            print(shot)
            return
    print(-1)


solve()
